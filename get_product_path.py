def get_product_path(full_path):
	s = full_path.split('/')
	#return '/'.join([s[1], s[2]])
	print('/'.join([x for x in s[:3] if x != 'ps']))

get_product_path('ps/BIS/BIS_8/8.4.0/mib')
get_product_path('BIS/BIS_8/8.4.0/mib')
