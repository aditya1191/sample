#!/usr/bin/python3

""" 

{'salary': 1111258, 'to_messages': 3627, 'deferral_payments': 'NaN', 
'total_payments': 8682716, 'loan_advances': 'NaN', 'bonus': 5600000,
 'email_address': 'jeff.skilling@enron.com', 'restricted_stock_deferred': 'NaN', 
 'deferred_income': 'NaN', 'total_stock_value': 26093672, 'expenses': 29336, 
 'from_poi_to_this_person': 88, 'exercised_stock_options': 19250000, 'from_messages': 108, 
 'other': 22122, 'from_this_person_to_poi': 30, 'poi': True, 'long_term_incentive': 1920000,
   'shared_receipt_with_poi': 2042, 'restricted_stock': 6843672, 'director_fees': 'NaN'}



    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import joblib

enron_data = joblib.load(open("../final_project/final_project_dataset.pkl", "rb"))

# print(enron_data.items())
# poicount = 0
# for key, (key2, val) in enumerate(enron_data.items()):
#     if (val["poi"] is True):
#         poicount = poicount + 1

# poicount = [val["poi"] for key, (key2, val) in enumerate(enron_data.items()) if val["poi"] is True]

# print("no. of poi ppl : " + str(poicount.count(True)))
# print("person : " + key2 + " poi : " + len(val["poi"] is True))

# poicount = [key2 for key, (key2, val) in enumerate(enron_data.items()) if val["poi"] is True]

# print(poicount)
# print(enron_data["SKILLING JEFFREY K"])

# What is the total value of the stock belonging to James Prentice?

# print(enron_data.get("PRENTICE JAMES").get("total_stock_value"))

# How many email messages do we have from Wesley Colwell to persons of interest ?

# print(enron_data.get("COLWELL WESLEY").get("from_this_person_to_poi"))

# What’s the value of stock options exercised by Jeffrey K Skilling?

# print(enron_data.get("SKILLING JEFFREY K").get("exercised_stock_options"))


# Of these three individuals (Lay, Skilling and Fastow),
# who took home the most money (largest value of “total_payments” feature)?
# How much money did that person get?
# top_brass = [("SKILLING JEFFREY K", enron_data.get("SKILLING JEFFREY K")),("FASTOW ANDREW S", enron_data.get("FASTOW ANDREW S")),
#              ("LAY KENNETH L",enron_data.get("LAY KENNETH L"))]


# # print(enron_data.get("LAY KENNETH L"))
# # print(top_brass)
# hiest = 0
# richest_ahole = ()

# for k in top_brass:
#     if (hiest < k[1]["total_payments"]):
#         hiest = k[1]["total_payments"]
#         richest_ahole = k

# print(richest_ahole[0])

# print([(k1, max(v["total_payments"])) for k1, v in top_brass])

# print(enron_data[max(int(enron_data, key= lambda v: enron_data[v]["total_payments"]))])

# tp_lst = [ed["total_payments"] for ed in enron_data.values()]
# tp_lst = [ed for ed in tp_lst if str(ed) != "NaN"]
# print(max(tp_lst))
# print([k2 for k2 in [ed for ed in enron_data.items()] if k2["total_payments"] == max(tp_lst)])
# print([(k2, v2) for i, (k2, v2) in enumerate(list(enron_data.items())) if v2["total_payments"] == max(tp_lst)])
# print(enron_data.get("TOTAL"))

# assgnd = (max(v1["salary"]) for k, (k1, v1) in enumerate(enron_data.items()))

# print(next(assgnd))
#######################################################################
# Yes, 95 have a quantified salary. 111 have a known email address.

# with_sal = [k1 for k, (k1, v1) in enumerate(enron_data.items()) if v1["salary"] != "NaN"]
# print(len(with_sal))

# with_mailAdd =  [k1 for k,(k1, l1) in enumerate(enron_data.items()) if l1["email_address"] != "NaN"]
# print(len(with_mailAdd))

########################################################################
# what percentage had total_payments as NaN
assgnd = [k1 for k, (k1, v1) in enumerate(enron_data.items()) if v1["total_payments"] == "NaN"]
print(len(assgnd))
print(len(enron_data.items()))
# print(len(assgnd)/len(enron_data.items()) * 100)

#######################################################################
# How many POIs in the E+F dataset have “NaN” for their total payments?
# What percentage of POI’s as a whole is this?

# assgnd = [k1 for k, (k1, v1) in enumerate(enron_data.items()) if v1["poi"] is True
          # and v1["total_payments"] == "NaN"]

# print(len(assgnd))
'''
Yes, correct. No training points would have "NaN" for total_payments when the class label is "POI"

8.25age + 
let me show you just what it looks like 
so you have some reason to understand why its important

you will have a lower score on your testing data compared to the 
training data  

just using sort of your intuistic heuristic for what the best might mean ?

heuristic
enabling someone to discover or learn something for themselves.

there can be multiple lines that minimize absolute error Σ|error| and only one line 
that  can minimize sumofsqrderr Σerror^2
  
'''



# print(len(enron_data.items()))