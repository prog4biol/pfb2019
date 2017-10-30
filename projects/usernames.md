# TOC

1. [Log onto remote machines](#log-onto-remote-machines)
2. [Login user names](#log-in-user-names)
3. [Starting jupyter-notebooks](#starting-jupyter-notebooks)

## Log onto remote machines

Log in using your ssh key (permission 0400). Find your usr name below. Replace 'xyz' with your group name.

`ssh -i key.pem usr@xyz.programmingforbiology.org`

To create a tunnel for your browser to diaplay the jupyter notebook add the `-L` switch. Use the remote port designated to you in the table below, followed by ":localhost:", and any local port on your machine. The local port can be the same as your remote port.  

`ssh -L remote_port:localhost:local_port  -i key.pem usr@xyz.programmingforbiology.org`

## Login user names

Name | username | remote_port |
-----|-----------|-------------|
Mr. Jessen  Bredeson	| jbres | 11111
Dr. Michael S Campbell |	mcamp | 11112
Ms. Xengie  Doan |	xdoan| 11113
Mr. Lukas  Kuderna |	lkude | 11114
Dr. Demitri  Muna |	dmuna | 11115
Dr. Simon E Prochnik	| sproc | 11116
Dr. Sofia M Robb |	srobb | 11117
Ms. Ying  Sun	| ysun | 11118
Mr. Agneesh  Barua |	abaru | 11119
Ms. Nathalia  Graf-Grachet |	ngraf | 11120 
Dr. Adam M Blanchard |	ablan | 11121
Mr. Mitchell T Lavarias	| mlava | 11122 
Dr. Chingiz  Underbayev |	cunde | 11123
Ms. Shasta E Webb	| swebb | 11124
Ms. Sabriya  Syed |	ssyed | 11125
Mr. Andrew J Behrens	| abehr | 11112
Mr. William J Brewer |	wbrew  | 11113
Dr. Carrie L Iwema |	ciwen | 11114
Mr. Zachary A Kemmerer |	zkemm | 11115
Dr. Jason M Singer |	jsing | 11116
Dr. Guillaume J Bauchet |	gbauc | 11117
Dr. Meredith L Cenzer |	mcenz | 11118
Mr. James J Miller |	jmille | 11119
Nick | nick | 11120
Xuan zhang | 	xzhan | 11121
Bryan Ngo	| bngo | 11122
 
## starting jupyter-notebooks

`jupyter-notebook --port=remote_port`

paste the url that is printed out when you run the above command into your browser
