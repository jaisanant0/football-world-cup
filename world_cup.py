import pandas as pd
import matplotlib.pyplot as plt
import sys

if len(sys.argv) < 3 :
    print("[-] Required arguments are not entered ")
    sys.exit(0)

#paths
filepath=sys.argv[1]
plotpath=sys.argv[2]
year=sys.argv[3]

#read csv
world_cup_csv=pd.read_csv(filepath)
world_cup_df=pd.DataFrame(world_cup_csv)

#check year
wc_season=set(list(world_cup_df['season']))
if int(sys.argv[3]) not in wc_season :
        print("[-] Unfortunately World Cup did not happen in " + str(year))
        sys.exit(0)
        
#dataframe as per year        
world_cup_df_year=world_cup_df[world_cup_df['season'] == int(year)]
group_by_team=world_cup_df.groupby(world_cup_df_year['team'])


#team names        
print("[+] Teams Names : \n")
group_names=[names for names,groups in group_by_team]
for i,names in enumerate(group_names) :
    print(str(i+1)+ "." + names)
    
team_name=input("\n[+] Enter the team name : ")
get_group_name=((group_by_team.get_group(team_name)).drop(columns=['team','season'],axis=1)).reset_index(drop=True)  

#visualization
fig,ax=plt.subplots(1,1)
plt.subplots_adjust(top=.95,bottom=.15,right=.99,left=.04)
get_group_name.plot(ax=ax,kind='bar',legend='Metrices',xticks=get_group_name.index,figsize=(15,10),title=team_name.upper())
ax.legend(fontsize='small')
ax.set_xlabel('Player Name')
ax.set_ylabel('Z-score')
ax.set_xticklabels(get_group_name['player'],rotation=45,fontsize='x-small')

#save and show plot
plt.savefig(plotpath+str('.jpeg'),dpi=400,bbox_inches='tight')
plt.show()

    
