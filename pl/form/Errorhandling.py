try:
    print(2/0)
except Exception as e:
       if str(e)=="division by zero":
             print ("لطفا عدد را تقسیم بر صفر نکنید")