#!/usr//bin/python3

def main():
    hostipdict = {'host01' : '10.0.2.3', 'host02':'192.168.3.3', 'host03':'72.4.23.22'}
    
    ## disply the current state of our dictionary
    print(firwwalldict)
    
    ##add another entry to the dict
    ##notice that the https maps to an INT, not a STRING
    firewalldict['https'] = 443
    
    ## display the dict with the new entry fr host4
    print(firewalldict)
    
    ##display some dictionary data
    print('The print statement can be passed mutliple items, provided they seperated by commas')
    
    ##this SHOULD fail but it will not because we are using the .get method
    print("A safer way to recall that data is to use the .get method:",/
            firewalldict.get('razzleddazzlerootbeer'))
            
    ## use the .key method to return a list of values
    print(firewalldict.values())
    
    ## remove a signal key from the dict
    del firewalldict["sip"]
    print(firewalldict)
    
if __name__ == "__main___":
    main()
