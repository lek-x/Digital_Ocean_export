import requests
import json
print("Digital Ocean export script \n")

drop = "dropelts"
keys = "ssh_keys"
image = "images"

### Function for choosing endpoints
def chf(a,**kwargs):
        match choose:
                case 1:
                        #print("List all", drop ,"\n")
                        endpt ="https://api.digitalocean.com/v2/droplets"
                        filename = "drop_list"
                case 2:
                        #print("List all",keys,"\n")
                        endpt = "https://api.digitalocean.com/v2/account/keys"
                        filename = "keys_list"
                case 3:
                        #print("List all", image,"\n")
                        endpt = "https://api.digitalocean.com/v2/images"
                        filename = "image_list"
                #case 0:
                        #print("Exit")

        return endpt,filename

### Function for authorization
def auth(endpt,filename):
        auth_header=input("Insert your authorization token\n>>>")
        data = {}
        headers = {"Authorization": "Bearer none", 'Content-Type': 'application/json'}
        headers["Authorization"] = str("Bearer")+ " " + str(auth_header)
      
        x = requests.get(str(endpt),data=data, headers=headers).json()
        return x


print("####Info section####")
print("""Digital Ocean API endpoints: \n
1. droplets: https://api.digitalocean.com/v2/droplets
2. ssh_keys: https://api.digitalocean.com/v2/account/keys
3. images: https://api.hetzner.cloud/v1/images
0. Exit\n""")


### Waiting user's input
choose = int(input("Choose endpoint \n >>"))

### Using functions
res=(chf(choose)) 

### Saving data       
with open ((res[1] + ".json"), "a") as file:
        file.write("\n")
        file.write(json.dumps(auth(res[0],res[1])))

### Exiting		
print("Done! Check your directory for ",res[1],".json \n")
input("Press any key to exit")


exit()        
