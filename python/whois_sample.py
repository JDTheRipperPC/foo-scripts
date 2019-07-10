import pprint
import pythonwhois


root_server = pythonwhois.net.get_root_server('google.com')
print(root_server)
print()

whois = pythonwhois.get_whois('google.com')
print(whois.items())
print()

whois_raw = pythonwhois.net.get_whois_raw('google.com')
pprint.pprint(whois_raw)
