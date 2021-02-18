import pymongo

client = pymongo.MongoClient("mongodb+srv://Travis:Rally@accounts.gqj8e.mongodb.net/Rally?retryWrites=true&w=majority")
database = client["Rally"]
collection = database["Topics"]

def setupTopic(idNum, name, description):
    topics ={
        "idNum": idNum,
        "name" : name,
        "description": description
    }
    collection.insert_one(topics)

def getTopics():
    return collection.find({})
# setupTopic(1, "Climate Change", "Earth’s climate is now changing faster than at any point in the history of modern civilization, primarily as a result of human activities. Global climate change has already resulted in a wide range of impacts across every region of the country and many sectors of the economy that are expected to grow in the coming decades. ")
# setupTopic(2, "Racial Injustice", "Racial inequality identifies the social inequality and advantages and disparities that affect different races within the United States. These can also be seen as a result of historic oppression, inequality of inheritance, or overall racism and prejudice, especially against minority groups.")
# setupTopic(3, "LGBTQ+", "In too many countries, being lesbian, gay, bisexual, transgender or intersex (LGBTI) means living with daily discrimination. This discrimination could be based on your sexual orientation (who you’re attracted to); gender identity (how you define yourself, irrespective of your biological sex), gender expression (how you express your gender through your clothing, hair or make-up), or sex characteristics (for example, your genitals, chromosomes, reproductive organs, or hormone levels.)")
# setupTopic(4, "Democratic Party", "The Democratic Party is one of the two major contemporary political parties in the United States")
# setupTopic(5, "Republican Party", "The Republican Party is one of the two major contemporary political parties in the United States")
# setupTopic(6, "Education", "In the modern world, economic growth and the spread of democracy have raised the value of education and increased the importance of ensuring that all children and adults have access to high-quality, effective education. Modern education reforms are increasingly driven by a growing understanding of what works in education and how to go about successfully improving teaching and learning in schools.")
# setupTopic(7, "Gender Inequality", "Gender inequality is the social process by which men and women are not treated as equals. The treatment may arise from distinctions regarding biology, psychology, or cultural norms. Some of these distinctions are empirically-grounded while others appear to be socially constructed.")
# setupTopic(8, "Gun Violence", "Gun violence is a leading cause of premature death in the U.S. Guns kill more than 38,000 people and cause nearly 85,000 injuries each year. As a longtime advocate for violence prevention policies, APHA recognizes a comprehensive public health approach to addressing this growing crisis is necessary.")