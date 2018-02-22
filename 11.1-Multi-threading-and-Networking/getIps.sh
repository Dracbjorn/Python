for i in $(nmap -n -sn 172.16.28.0/24 | grep -B1 "Host is up" | grep -v "Host is up" | cut -d " " -f5); do
  ping -c 1 $i | grep "ttl=64" &>/dev/null
  if [ $? -eq 0 ]; then 
     echo $i 
  fi
done
