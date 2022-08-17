function itoh(src) {
    load=(d)=>{
        s='';b=0;t=0;l=1;
        for(i=0; s.length<l; i += (i%4-2)?1:2){
            b += 2;
            t = t * 4 + (d[i] % 4);
            if(b==32){
                l = t;
                t = 0;
            }if(b>32&&!(b%8)){
                s += String.fromCharCode(t);
                t = 0;
            }
        }
        document.lastChild.innerHTML = decodeURIComponent(escape(s));
    }
    v=document.createElement('canvas')
    v.height=10000;
    v.width=10000;
    g = new Image();
    g.crossOrigin = 'Anonymous';
    g.onload = () => {
        c = v.getContext('2d');
        c.drawImage(g, 0, 0);
        load(c.getImageData(0,0,g.width,g.height).data);
    }
    g.src = src;
}
