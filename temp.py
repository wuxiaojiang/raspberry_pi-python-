import time
def cpu_temp():
    tf = open('/sys/class/thermal/thermal_zone0/temp')
    ct = tf.read()
    tf.close()
    return float(ct)/1000

def main():
    o = file("temp.txt","w+")
    for i in range(10):
        temp = cpu_temp()
        print temp
        t = i+1
        o.write('(')
        o.write("%s"%t)
        o.write(')')
        o.write(str(temp))
        o.write(' ')
        time.sleep(3)
    o.close()

if __name__ == '__main__':
    main()
