import pymupdf,glob,os,re,datetime as dt,json,sys
def parse(path):
    d=pymupdf.open(path); out=[]
    for p in d:
        W=p.get_text('words')
        dates=[(w,dt.datetime.strptime(w[4],'%d-%b-%y').date()) for w in W if re.fullmatch(r'\d\d-[A-Z][a-z]{2}-\d\d',w[4])]
        if len(dates)<14: continue
        dates=sorted(dates,key=lambda x:x[0][0])[:14]
        cx=[((w[0]+w[2])/2,dd) for w,dd in dates]
        colw=(cx[-1][0]-cx[0][0])/13
        pays=[w for w in W if re.fullmatch(r'\d{5,8}',w[4]) and w[0]<cx[0][0]-colw]
        pays=sorted(pays,key=lambda w:w[1])
        for i,pw in enumerate(pays):
            y0=pw[1]-2; y1=(pays[i+1][1]-2) if i+1<len(pays) else pw[3]+18
            roww=[w for w in W if y0<=(w[1]+w[3])/2<y1]
            name=' '.join(w[4] for w in sorted(roww,key=lambda w:w[0]) if w[0]<cx[0][0]-colw/2 and w[4]!=pw[4])
            status=None
            cells={}
            for w in roww:
                x=(w[0]+w[2])/2
                if x<cx[0][0]-colw/2: continue
                j=min(range(14),key=lambda k:abs(cx[k][0]-x))
                if abs(cx[j][0]-x)>colw*0.6: continue
                cells.setdefault(j,[]).append((w[0],w[4]))
            row={}
            for j in range(14):
                toks=[t for _,t in sorted(cells.get(j,[]))]
                s=''.join(toks)
                row[str(cx[j][1])]=s if s else '-'
            out.append({'file':os.path.basename(path),'page':p.number,'pay':pw[4],'name':re.sub(r'^[A-Z]\s*-\s*','',name).strip(),'cells':row})
    return out
if __name__=='__main__':
    allr=[]
    for f in sys.argv[1:]: allr+=parse(f)
    json.dump(allr,open('/tmp/claude-0/-home-user/6625dff5-a18f-544c-a62c-8ea1e8b9d28c/scratchpad/rows.json','w'))
    print(len(allr),'rows')
