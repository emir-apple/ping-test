from tkinter import *
from pythonping import ping
window = Tk()
window.title("quadew's ping test")
window['background']='#1b2838'
window.geometry("246x118")

def get():
    result=ping( '1.1.1.1', count=1,size=40,df=True)
    resultg=ping( '8.8.8.8', count=1,size=40,df=True)
    resulty=ping( '77.88.8.8', count=1,size=40,df=True)
    resulto=ping( '208.67.222.222', count=1,size=40,df=True)
    resultno=ping( '198.153.192.1', count=1,size=40,df=True)
    resultlev=ping( '209.244.0.3', count=1,size=40,df=True)
    resultep=ping( '52.47.193.251', count=1,size=40,df=True)
    resultste=ping( '23.62.138.105', count=1,size=40,df=True)
    
    res.set(result.rtt_avg_ms)
    resg.set(resultg.rtt_avg_ms)
    resy.set(resulty.rtt_avg_ms)
    reso.set(resulto.rtt_avg_ms)
    resno.set(resultno.rtt_avg_ms)
    reslev.set(resultlev.rtt_avg_ms)
    resep.set(resultep.rtt_avg_ms)
    resste.set(resultste.rtt_avg_ms)

res= StringVar()
resg= StringVar()
resy= StringVar()
reso= StringVar()
resno= StringVar()
reslev= StringVar()
resep= StringVar()
resste= StringVar()

ttc=Label(window, text="Cloudflare:",bg="orange").grid(row=2)
ttg=Label(window, text="Google:",bg="green").grid(row=3,column=0)
tty=Label(window, text="Yandex:",bg="yellow").grid(row=4,column=0)
tty=Label(window, text="OpenDns:",bg="red").grid(row=5,column=0)
ttno=Label(window, text="NorthonDns:",bg="#f5c242").grid(row=5,column=0)
ttnlev=Label(window, text="LevelDns:",bg="#db6600").grid(row=6,column=0)
ttep=Label(window, text="EpicGames-EU:",bg="black",fg='white').place(x=108, y=0)
ttste=Label(window, text="Steam-EU:",bg="Blue",fg='white').place(x=108, y=22)

ttcf=Label(window, text="6", textvariable=res, bg="#1b2838",fg='white').grid(row=2,column=1)
ttgf=Label(window, text="6", textvariable=resg, bg="#1b2838",fg='white').grid(row=3,column=1)
ttyf=Label(window, text="6", textvariable=resy, bg="#1b2838",fg='white').grid(row=4,column=1)
ttyo=Label(window, text="6", textvariable=reso, bg="#1b2838",fg='white').grid(row=5,column=1)
ttyle=Label(window,text="6", textvariable=reslev, bg="#1b2838",fg='white').grid(row=6,column=1)
ttgep=Label(window,text="6", textvariable=resep, bg="#1b2838",fg='white').place(x=195, y=0)
ttgste=Label(window,text="6", textvariable=resste, bg="#1b2838",fg='white').place(x=174, y=22)

button1 =Button(window,text="Start", bg="#66c0f4", fg="black", command=get,relief=RAISED,width='10')
button1.place(x=125, y=60)

mainloop()