#!/usr/bin/python
# -*- coding: utf8 -*-
import elasticsearch
import pprint
import time
import datetime
import random
import pytz
import json
import string
import sys

es = elasticsearch.Elasticsearch(['localhost'],port=9400,http_auth=("elastic","Elastic2018!"))

mapping = {
    "mappings" : {
            "sample_ecommerce" : {
                "properties" : {
                        "timestamp" : { "type": "date" },
                        "dayOfWeek" : { "type": "integer" },
                        "transaction_id" : { "type": "integer" },
                        "customer_id" : { "type": "integer" },
                        "customer_name" : { "type": "keyword" },
                        "product_id" : { "type": "integer" },
                        "product_name" : { "type": "keyword" },
                        "product_description" : { "type": "text" },
                        "product_price" : { "type": "float" },
                        "product_category" : { "type": "keyword" },
                        "review_id" : { "type": "integer" },
                        "review_description" : { "type": "text" },
                        "review_rating" : { "type": "integer" },
                        "review_timestamp" : { "type": "date" },
                }
            }
    }
}

pprint.pprint(mapping)

es.indices.create(index="sample_ecommerce",body=mapping, ignore=400)



#customers
#customer id, customer name
customers = [[1,'Nicolette Good'],[2,'Mallie Redeker'],[3,'Matha Osmun'],[4,'Marsha Mcdow'],[5,'Gala Falcon'],[6,'Katerine Mumma'],[7,'Felisa Koerber'],[8,'Dannielle Hopf'],[9,'Gena Bundick'],[10,'Vesta Skalski'],[11,'Verla Tisby'],[12,'Wilson Pane'],[13,'Gidget Yaple'],[14,'Clyde Mccloskey'],[15,'Quentin Slane'],[16,'Shelly Montesano'],[17,'Beatriz Stanberry'],[18,'Sung Rosendahl'],[19,'Sau Natale'],[20,'Santana Dino'],[21,'Virgina Eisenmann'],[22,'Geraldo Gagnon'],[23,'Glady Geraghty'],[24,'Yulanda Cowher'],[25,'Clara Luciano'],[26,'Katlyn Agar'],[27,'Ruth Martinek'],[28,'Sharice Wiese'],[29,'Ronny Steeves'],[30,'Keva Fosdick'],[31,'Candie Gardea'],[32,'Magdalen Derksen'],[33,'Julie Pompey'],[34,'Marian Gourley'],[35,'Wonda Skelly'],[36,'Shameka Oster'],[37,'Darrick Pacelli'],[38,'Angeles Lockhart'],[39,'Ching Johnston'],[40,'Stephania Hoffman'],[41,'Stephani Trafton'],[42,'Valerie Hadsell'],[43,'Norman Montenegro'],[44,'Melvin Degenhardt'],[45,'Phoebe Fenn'],[46,'Pamela Hersom'],[47,'Christinia Mohammed'],[48,'Eliza Clune'],[49,'Davida Petrick'],[50,'Sparkle Garon'],[51,'Frank Mork'],[52,'Lucilla Bezanson'],[53,'Lashawnda Kerfoot'],[54,'Alise Araiza'],[55,'Alta Waldo'],[56,'Magaly Stgelais'],[57,'Catherine Kondo'],[58,'Darrin Firestone'],[59,'Reuben Gideon'],[60,'Perla Kirkbride'],[61,'Cody Ehlert'],[62,'Joaquin Hardy'],[63,'Debera Luck'],[64,'Julia Monfort'],[65,'Charmain Drovin'],[66,'Gertrude Winn'],[67,'Eleonor Joslin'],[68,'Chana Tharp'],[69,'Kristeen Hartshorn'],[70,'Erika Gabbard'],[71,'Cristine Bergan'],[72,'Jacquelin Stenson'],[73,'Chelsie Schildgen'],[74,'Elba Robitaille'],[75,'Kayleen Tasker'],[76,'Lavern Pelosi'],[77,'Cathleen Minks'],[78,'Jeffie Silvestri'],[79,'Jutta Lira'],[80,'Sonny Torrez'],[81,'Malia Sapien'],[82,'Justina Utter'],[83,'Roxanne Hammett'],[84,'Barbara Raborn'],[85,'Dinorah Poplin'],[86,'Scarlet Guy'],[87,'Leesa Jiggetts'],[88,'Inger Parrett'],[89,'Carry Paul'],[90,'Cordie Vangieson'],[91,'Rocio Chrzanowski'],[92,'Christia Goetsch'],[93,'Darwin Speegle'],[94,'Johnnie Craine'],[95,'Kimi Burfield'],[96,'Vilma Champ'],[97,'Rana Belknap'],[98,'Lianne Vaden'],[99,'Bryant Forry'],[100,'Camelia Vines'],[101,'Flavia Mcconnaughey'],[102,'Vernell Veitch'],[103,'Ladawn Sexson'],[104,'Florrie Jennette'],[105,'Halley Lover'],[106,'Tambra Heinen'],[107,'Caitlin Reach'],[108,'Elda Bordeau'],[109,'Joy Tenenbaum'],[110,'Tania Teran'],[111,'Scotty Delk'],[112,'Cassie Toscano'],[113,'Letisha Penton'],[114,'Willa Walquist'],[115,'Bethann Lasso'],[116,'Chloe Lisi'],[117,'Erminia Mackley'],[118,'Susanna Mickelsen'],[119,'Iluminada Sponaugle'],[120,'Tula Cooke'],[121,'Ming Brunk'],[122,'Rosanna Bartow'],[123,'Murray Kniffen'],[124,'Clarine Eisenhart'],[125,'Dee Saltzman'],[126,'Cheyenne Lower'],[127,'Clint Liedtke'],[128,'Claris Hashimoto'],[129,'Lakenya Nygard'],[130,'Lura Martello'],[131,'Rhoda Esses'],[132,'Nickolas Selle'],[133,'Sharan Bowden'],[134,'Elvia Rahimi'],[135,'Vivan Pellegrin'],[136,'Marianna Cudjoe'],[137,'Caprice Retana'],[138,'Clementine Person'],[139,'Zelda Castonguay'],[140,'Rhea Meiser'],[141,'Eileen Prum'],[142,'Elroy Boylan'],[143,'Sharon Couey'],[144,'Shawnta Pareja'],[145,'See Defrank'],[146,'Mohamed Mahood'],[147,'Olin Lard'],[148,'Hattie Filkins'],[149,'Rayford Augustine'],[150,'Tess Quigg'],[151,'Latoyia Tibbitts'],[152,'Magdalen Bartow'],[153,'Judi Hoch'],[154,'Franklyn Numbers'],[155,'Signe Spidle'],[156,'Stacia Burris'],[157,'Shari Kroeker'],[158,'Thora Figura'],[159,'Emmanuel Chamness'],[160,'Shelton Lemmer'],[161,'Apolonia Graziano'],[162,'Trudy Cabell'],[163,'Nyla Bondurant'],[164,'Wilson Romaine'],[165,'Irvin Monroig'],[166,'Carey Gassett'],[167,'Lee Gatchell'],[168,'Lasandra Smothers'],[169,'Shayla Bryer'],[170,'Delcie Kime'],[171,'Pauline Bottomley'],[172,'Mae Pinckney'],[173,'Lura Horne'],[174,'Arnetta Strickland'],[175,'Cira Marlar'],[176,'Gerardo Taube'],[177,'Carma Timothy'],[178,'Hayley Olszewski'],[179,'Wendell Shelburne'],[180,'Vernita Perrier'],[181,'Genevie Hollow'],[182,'Necole Goodspeed'],[183,'Tori Perras'],[184,'Lucile Nicoletti'],[185,'Cathleen Bezio'],[186,'Jonathon Fanning'],[187,'Alyce Pinkowski'],[188,'Sheldon Nilsson'],[189,'Sammy Livsey'],[190,'Rea Angert'],[191,'Brandy Harriston'],[192,'Madonna Hidalgo'],[193,'Izetta Blakeley'],[194,'Kiesha Marcell'],[195,'Sebastian Moncada'],[196,'Kaye Opie'],[197,'Mechelle Elfrink'],[198,'Fredericka Troia'],[199,'Kendall Selvage'],[200,'Trish Zimmermann']]

#products
#product id, product name, description, price, category
products = [[02,"Elasticsearch Tank", "Keep the laidback vibes going with this essential tank top by Elasticsearch. The Classic Tank Top has a U-neckline and the brand's signature graphic printed across the front", 25.00, "Clothing"], [03,"Beats Crew Neck", "A modern and easy statement sweatshirt with Beats branding.", 55.00, "Clothing"]]

#popular products
popular_products = [[01,"Kibana V-Neck", "An embroidered Kibana logo brands the chest of a wardrobe-staple cotton T-shirt styled with a classic V-neck profile.", 35.00, "Clothing"], [04,"Logstash Hoody", "A supersoft fleece sweatshirt featuring a hood with drawstrings, half-zip neckline, Logstash icon at left chest, colorblocking, pouch pocket and ribbed trim, Slim Fit, Imported", 85.00, "Clothing"]]

#reviews
#review, rating
#at run time: review_id, customer id, customer name
reviews_and_ratings = [["review text1", 3], ["review text2", 5], ["review text3", 1]]



# fresh stuff
transaction_id = 100000
review_id = 10000
probability_review = 0.1
probability_popular = 0.4
business_hours = (8,9,10,16,17,18,21,22,23)
weekend_hours = (1,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23)



while True:
    try:
        transactions = {}
        transactions['timestamp'] = str(pytz.utc.localize(datetime.datetime.utcnow())).replace(' ','T')
        transactions['dayOfWeek'] = pytz.utc.localize(datetime.datetime.utcnow()).weekday()
        transactions['transaction_id'] = transaction_id
        product = random.choice(popular_products) if random.random() <= probability_popular else random.choice(products)
        customer = random.choice(customers)

        transactions['product_id'] = product[0]
        transactions['product_name'] = product[1]
        transactions['product_description'] = product[2]
        transactions['product_price'] = product[3]
        transactions['product_category'] = product[4]

        transactions['customer_id'] = customer[0]
        transactions['customer_name'] = customer[1]

        review_ingest = False if random.random() <= probability_review else True
        if review_ingest == True:
            review = random.choice(reviews_and_ratings)
            review_timestamp = pytz.utc.localize(datetime.datetime.utcnow()) + datetime.timedelta(days=random.randint(2,30))
            transactions['review_timestamp'] = str(datetime.datetime(review_timestamp.year, review_timestamp.month, review_timestamp.day, random.choice(weekend_hours), random.randint(0,60), random.randint(0,60))).replace(' ','T')
            transactions['review_id'] = review_id
            #transactions['review_description'] = review[0]
            transactions['review_rating'] = review[1]
            review_id += 1

        #print and write to file
        pprint.pprint(transactions)
        es.index(index="sample_ecommerce", doc_type="doc", id=transactions['transaction_id'], body=transactions)

        # iterate
        transaction_id += 1

    except:
        print "Error contacting elasticsearch"
    print "sleeping for 5 sec"
    time.sleep(5)
