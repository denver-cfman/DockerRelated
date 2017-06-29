import docker
dcl = docker.from_env()
"""
for i in dcl.containers.list():
	i.stop()
	#i.remove()
"""

for i in dcl.containers.list():
	print str(i.name) + " / " + str(i.stats())
	#i.remove()
