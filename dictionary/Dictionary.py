name_of_the_cities={
        "Charlottetown": {
        "Population": 40488,
        "Area": 44.34,
        "Growth": +2.5
                    },
        "Summerside":
        {
        "Population": 15553,
        "Area": 28.49,
        "Growth": +1.2
                     },
        "Stratford": {
        "Population": 10973,
        "Area": 22.53,
        "Growth": +2.8
                     },

     "Cornwall": {
        "Population": 6039,
        "Area": 28.19,
        "Growth": +2.8
                    },

      "Montague": {
        "Population": 2031,
        "Area": 3.16,
        "Growth": +0.1
                      },

     "Kensington": {
        "Population": 1856,
        "Area": 3.01,
        "Growth": +3.9
                      },

     "Alberton": {
        "Population": 1288,
        "Area": 4.52,
        "Growth": +6.4

                   },

     "Souris": {
        "Population": 908,
        "Area": 3.47,
        "Growth": -5.9

                   },

     "O Leary": {
        "Population": 859,
        "Area": 1.68,
        "Growth": +1.3

                   },

     "Borden-Carleton": {
        "Population": 765,
        "Area": 12.99,
        "Growth": +1.3

                   }
    
    }

f=open("name of the cities.txt", "w")



x=input("enter the city name you want to know about: " )
y=input("enter what you want to know  about the city: " )


if y=="Population":
    print("approximate population of ", x,"is ",name_of_the_cities[x][y])
elif y=="Area":
    print("area of ", x, " is ", name_of_the_cities[x][y])
elif y=="Growth":
    print("from last year growth of ", x, "is ", name_of_the_cities[x][y])
else:
    

    print("we don't have that information")


while x!=1:
    x=input("enter the city name you want to know about or 1 if you want to quit: " )
    y=input("enter what you want to know  about the city: " )
    


    if y=="Population":
        
        print("approximate population of ", x,"is ",name_of_the_cities[x][y])
    elif y=="Area":
        print("area of ", x, " is ", name_of_the_cities[x][y])
    elif y=="Growth":
        print("from last year growth of ", x, "is ", name_of_the_cities[x][y])
    else:
    

        print("we don't have that information")
    

