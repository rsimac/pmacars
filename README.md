# pmacars
simple python ACARS utility for x-plane

# background
after x-plane and vatsim flights, it would be great to have an automated way to submit your flight detals to your virtual airline using simple and lightweight, non-intrusive command line utility, based on existing data fields from x-plane and vatsim

## sample usage
1. Set the x-plane data output to file (Data.txt) for following data fields as documented at https://www.x-plane.com/kb/data-set-output-table/
```
    real_time,totl_time,missn_time,timer_time,zulu_time,local_time,hobbs_time,
    Vind_kias,Vind_keas,Vtrue_ktas,Vtrue_ktgs,Vind_mph,Vtrue_mphas,Vtrue_mphgs,
    gear_0/1,wbrak_set,lbrak_add,rbrak_add,wbrak_part,N1_1_pcnt,N1_2_pcnt,N2_1_pcnt,N2_2_pcnt,
    fuel1_lb,fuel2_lb,fuel3_lb,fuel4_lb,fuel5_lb,fuel6_lb,
    empty_lb,payld_lb,fuel_totlb,jetti_lb,curnt_lb,maxim_lb,cg_ftref,gear_lb,gear_lb,gear_lb
```
2. Optionally, connect to Vatsim, file your flight plan, do the Vatsim things...

3. Fly

4. Land. Possibly in one piece. Shut down the engines. Have a cigar.

5. Start the pmacars: `python pmacars.py <full_path_to_xplane_data_txt> <your_vatsim_pilot_id>`. Pmacars will read your vatsim flight data. DO NOT exit pmacars. It still has to read xplane data file...

6. Exit X-Plane. This is mandatory, to flush and complete the Data.txt file. This will also disconnect from Vatsim, at least for some vatsim clients. That is ok, we already have vatsim flight data.

7. As prompted by still running pmacars, press ENTER and have pmacars read the xplane data.txt

8. Observe the output and use it to submit your flight details to your virtual airline

9. To be continued... See Issues under this project...
