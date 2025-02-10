from collections import deque

customers = deque()

def walk_in(customer):
    customers.append(customer)

def serviced():
    cust= customers.popleft()
    print(cust, 'leaves the shop')


walk_in('Vea')
walk_in('Mari')
walk_in('Maria')
serviced()
serviced()
walk_in('Maria')

print(customers)