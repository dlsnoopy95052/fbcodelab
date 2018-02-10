import subprocess 

def console(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out, err = p.communicate()
    out=out.decode().replace('\n','')
    err=err.decode().replace('\n','')
    return [p.returncode, out, err]

result = console('dir')
print('returncode: {}'.format(result[0]))
print('output: {}'.format(result[1]))
print('error: {}'.format(result[2]))