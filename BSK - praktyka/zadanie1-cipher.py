cipher = "oWdnreuf.lY uoc nar ae dht eemssga eaw yebttrew eh nht eelttre sra enic roertco drre . Ihtni koy uowlu dilekt  oes eoyrup sawsro don:wr dlimgclmhs.f"
ans = ''
i=0
while(i<len(cipher)-1):
    ans=ans+cipher[i+1]
    ans=ans+cipher[i]
    i=i+2
print(ans)