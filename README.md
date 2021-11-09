# pmacars
simple python ACARS utility for x-plane

## sample usage
1. Set the x-plane data output to file (Data.txt) for following data fields:
```
    real_time,totl_time,missn_time,timer_time,zulu_time,local_time,hobbs_time,
    Vind_kias,Vind_keas,Vtrue_ktas,Vtrue_ktgs,Vind_mph,Vtrue_mphas,Vtrue_mphgs,
    gear_0/1,wbrak_set,lbrak_add,rbrak_add,wbrak_part,N1_1_pcnt,N1_2_pcnt,N2_1_pcnt,N2_2_pcnt,
    fuel1_lb,fuel2_lb,fuel3_lb,fuel4_lb,fuel5_lb,fuel6_lb,
    empty_lb,payld_lb,fuel_totlb,jetti_lb,curnt_lb,maxim_lb,cg_ftref,gear_lb,gear_lb,gear_lb
```

2. Fly

3. Exit X-Plane

4. Run this utility and use the output to fill your flight log:
```
> python pmacars.py 'C:\Program Files (x86)\Steam\steamapps\common\X-Plane 11\Data.txt'
{'startup_zulu': '17:24', 'shutdown_zulu': '17:43'}
> 
```
