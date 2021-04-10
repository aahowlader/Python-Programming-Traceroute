from socket import *
import os
import sys
import struct
import time
import select
import binascii

label = '*************{0}*************'
ICMP_ECHO_REQUEST = 8
MAX_HOPS = 30
TIMEOUT = 2.0
TRIES = 1


# The packet that we shall send to each router along the path is the ICMP echo
# request packet, which is exactly what we had used in the ICMP ping exercise.
# We shall use the same packet that we built in the Ping exercise

def checksum(string):
    # In this function we make the checksum of our packet
    csum = 0
    countTo = (len(string) // 2) * 2
    count = 0

    while count < countTo:
        thisVal = (string[count + 1]) * 256 + (string[count])
        csum = csum + thisVal
        csum = csum & 0xffffffff
        count = count + 2

    if countTo < len(string):
        csum = csum + (string[len(string) - 1])

    csum = csum & 0xffffffff
    csum = (csum >> 16) + (csum & 0xffff)
    csum = csum + (csum >> 16)
    answer = ~csum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer

def get_name_or_ip(hostip)
    try:
        host = socket.gethostbyaddr(hostip)
        nameorip = nameorip = '{0} ({1})'.format(hostip, host[0])
        return nameorip
    except Exception:
        nameorip = '{0} (host name could not determinded)'.format(hostip)
        return nameorip

def build_packet():
    # create header and append check sum, Header is type (8), code(8), checksum(16),
id(16), seq(16)
    myChecksum = 0
    myID = os.getpid() & 0xFFFF

    # Return the current process i
    # make a dummy header with a 0 checksum
    # struct -- Interpret strings as packed binary data

    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, myID, 1)
    data = struct.pack("d", time.time())
    # Calculate the checksum on the data and the dummy header.
    myChecksum = checksum(header + data)

    # get the right checksum, and put in the header
    if sys.platform == 'darwin':
        # Convert 16-bit integers from host to network  byte order
        myChecksum = socket.htons(myChecksum) & 0xffff
    else:
        myChecksum = socket.htons(myChecksum)

    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, myID, 1)
    # Don’t send the packet yet , just return the final packet in this function.
    # Fill in end

    # So the function ending should look like this

    packet = header + data
    #return packet

def get_route(hostname):
    print(label.format(hostname))
    timeLeft = TIMEOUT

    for ttl in range(1, MAX_HOPS):
        for tries in range(TRIES):
            destAddr = socket.gethostbyname(hostname)
            # Fill in start
            # Make a raw socket named mySocket
            icmp = socket.getprotobyname("icmp")
            mySocket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
            # Fill in end

            mySocket.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, struct.pack('I', ttl))
            mySocket.settimeout(TIMEOUT)
            try:
                d = build_packet()
                mySocket.sendto(d, (hostname, 0))
                t = time.time()
                startedSelect = time.time()
                whatReady = select.select([mySocket], [], [], timeLeft)
                howLongInSelect = (time.time() - startedSelect)
                if whatReady[0] == []:  # Timeout
                    print(" * * * Request timed out.")
                    #tracelist1.append("* * * Request timed out.")
                    # Fill in start
                    # You should add the list above to your all traces list
                    #tracelist2.append(tracelist1)
                    # Fill in end
                recvPacket, addr = mySocket.recvfrom(1024)
                timeReceived = time.time()
                timeLeft = timeLeft - howLongInSelect
                if timeLeft <= 0:
                    print(" * * * Request timed out.")
                    #tracelist1.append("* * * Request timed out.")
                    # Fill in start
                    # You should add the list above to your all traces list
                    #tracelist2.append(tracelist1)
                    # Fill in end
            except timeout:
                continue

            else:
                # Fill in start
                # Fetch the icmp type from the IP packet
                icmpHeaderContent = recvPacket[20:28]
                types, code, checksum, packetID, sequence = struct.unpack("bbHHh", icmpHeaderContent)
                printname = get_name_or_ip(addr[0])
                # Fill in end
                if type == 11:
                    bytes = struct.calcsize("d")
                    timeSent = struck.unpack("d", recvPacket[28:28 + bytes])[0]
                    print(" %d rtt=%.Of ms %s" % (ttl,(timeReceived -t) * 1000, printname))
                elif type ==3:
                    bytes = struct.calcsize("d")
                    timeSent = struct.unpack("d", recvPacket[28:28 + bytes])[0]
                    print(" %d rtt=%.Of ms %s" % (ttl,(timeReceived -t) * 1000, printname))
                elif type ==0:
                    bytes = struct.calcsize("d")
                    timeSent = struct.unpack("d" recvPacket[28:28 + bytes])[0]
                    print(" %d rtt=%.of ms %s" % (ttl, (timeReceived - timeSent) * 1000, printname))
                    return
                else:
                    print("error")
                    break
            finally:
                mysocket.close()
def main():
    get-route("www.google.com")
    get_route("www.youtube.com")
    get_route("www.nyu.edu")
    get_route("www.nytimes.com")

print("--------------------------------------------")
print('www.google.com')
print("--------------------------------------------")
get_route("www.google.com")  # USA - North America

if __name__ == '__main__':
 main()
