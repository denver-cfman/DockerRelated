import docker
dcl = docker.from_env()
client_alive = False
for i in dcl.containers.list():
	if i.name == "zap_test1":
		""" Container is already Alive """
		client_alive = True
	else:
		print str(i.attrs['Config']['Image']) + "" + str(i.name) + "\n"
if not client_alive:
	dcl.containers.run(image='owasp/zap2docker-weekly',command='zap-webswing.sh -config api.key=foobar1234',detach=True, ports={'8080/tcp': 8080},name='zap_test1')
