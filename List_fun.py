import logging
logging.basicConfig(filename="List_fun.log", level=logging.INFO,format='%(name)s %(levelname)s %(asctime)s %(message)s')

l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]


class list_fun :
    def __init__(self,list_name):
        """ Taking any list """
        try:
            self.list_name = list_name
        except Exception as e:
            logging.exception(e)

    def list_reverse(self):
        """Reverse the given list"""
        try:

            logging.info("reverse of list")
            logging.info(self.list_name[::-1])
        except Exception as e:
            logging.exception(e)

    def length_of_list(self):
        """give the lengh of list """
        try:

            logging.info("length of the list is ")
            logging.info(len(self.list_name))
        except Exception as e:
            logging.exception(e)

    def Multiply_by_num(self,num):
        """list multiply by any number"""
        try:

            logging.info("list multiply by num %s",num)
            logging.info((self.list_name)*num)
        except Exception as e:
            logging.exception(e)

    def Append_list(self,list1):
        """append operation in list"""
        try:

            logging.info("list is append by ")
            logging.info(list1)
            self.list_name.append(list1)
            logging.info(self.list_name)
        except Exception as e:
            logging.exception(e)

    def div(self): #just to check the exception erron
        try:
            a=1
            b=0
            c=a/b
            logging.info("division is ",c)
        except Exception as e:
            logging.exception(e)

    def extend_list(self,list1):
        """extend the list """
        try:
            logging.info("extend the list by")
            logging.info(list1)
            self.list_name.extend(list1)
            logging.info(self.list_name)
        except Exception as e:
            logging.exception(e)

    def pop_list(self):
        """pop the list """
        try:
            logging.info("list before pop")
            logging.info(self.list_name)
            self.list_name.pop()
            logging.info("list after pop")
            logging.info(self.list_name)
        except Exception as e:
            logging.exception(e)

    def remove_from_list(self,list1):
        """funtion to remove from the list"""
        try:
            logging.info("element remove")
            logging.info(list1)
            self.list_name.remove(list1)
            logging.info("list after removing ")
            logging.info(list1)
            logging.info(self.list_name)
        except Exception as e:
            logging.exception(e)


    def discard_form_list(self,a):
        """discard from list"""
        try:
            logging.info("discrding element")
            logging.info(a)
            self.list_name.discard(a)
            logging.info("list after discrading")
            logging.info(self.list_name)
        except Exception as e:
            logging.exception(e)

    def List_in_list(self):
        """print list inside the list"""
        try:
            for i in self.list_name:
                if type(i)== list :
                    logging.info(i)
        except Exception as e:
            logging.exception(e)


    def Dict_in_list(self):
        """Dict inside the list"""
        try:
            for i in self.list_name:
                if type(i) == dict:
                    logging.info(i)
        except Exception as e:
            logging.exception(e)








l1 = list_fun(l)
l1.list_reverse()
l1.length_of_list()
l1.Multiply_by_num(2)
l1.Append_list("nagesh")
l1.div()
l1.extend_list(50)
l1.extend_list([12,13])
l1.extend_list("ineuron")
l1.extend_list(["ineuron"])
l1.pop_list()
l1.remove_from_list("nagesh")
l1.discard_form_list(3)
l2 = list_fun([10,20,30,40,50,60,7,0])
l2.discard_form_list(20)
l1.List_in_list()
l1.Dict_in_list()