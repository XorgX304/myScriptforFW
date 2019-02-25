import idaapi
ti = idaapi.tinfo_t()

addrofW32UserProbeAddress = LocByName("_W32UserProbeAddress")
addrofProbeForWrite = LocByName("__imp__ProbeForWrite@12")

for functionAddr in Functions():
   if "memcpy" in GetFunctionName(functionAddr):
		UserProbeXrefs = [GetFunctionName(UserProbeXref) for UserProbeXref in DataRefsTo(addrofW32UserProbeAddress)]				
		ProbeForWrite = [GetFunctionName(ProbeForWrite) for ProbeForWrite in DataRefsTo(addrofProbeForWrite)]
		
		xrefs = CodeRefsTo(functionAddr, False)
		for xref in xrefs:
			if GetMnem(xref).lower() == "call":        
				function_head = GetFunctionAttr(xref, idc.FUNCATTR_START)
				idaapi.get_tinfo2(function_head, ti)
				fi = idaapi.func_type_data_t()
				ti.get_func_details(fi)
				perfunc = []
				for i in xrange(fi.size()):
					if fi[i].name:
						perfunc.append(fi[i].name)
				
				if perfunc:
					func_name = GetFunctionName(function_head)
					#Start searching with Nt prefix for SSDT calls
					if func_name[0:3] == "_Nt":
						print func_name
					#Search functions that doesn't have W32UserProbeAddress
					if func_name not in UserProbeXrefs:
						print func_name
					#Search functions that doesn't have ProbeForWrite
					if func_name not in UserProbeXrefs:
						print func_name