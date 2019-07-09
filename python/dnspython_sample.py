import dns
import dns.query
import dns.resolver
import dns.zone

def print_answers(answers):
    for answer in answers:
        print(answer.response.to_text())
        print()

ansA = dns.resolver.query('google.com', 'A')
ansNS = dns.resolver.query('google.com', 'NS')
ansMX = dns.resolver.query('google.com', 'MX')
ansAAAA = dns.resolver.query('google.com', 'AAAA')

print_answers([ansA, ansNS, ansMX, ansAAAA])
