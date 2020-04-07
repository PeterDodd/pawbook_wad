import django, os, random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pawbook_wad.settings')
django.setup()

from pawbook.models import Post, Listing, UserProfile, PetPedia, Comment
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.images import ImageFile
from django.template.defaultfilters import slugify


# Populates the database for testing

def populate():
    testUsers = [
        ("John123", "John", "Smith", "I'm interested in LOLcats and stuff", "London"),
        ("Adam69", "Adam", "", "I sell puppies for decent prices hmu", ""),
        ("coolkid1337", "james", "", "Exotic pet trafficker", ""),
        ("tony86", "tony", "adams", "rock climber\ntwitter: tony86", "manchester"),
        ("sarahSmith", "sarah", "smith", "chef", "glasgow"),
        ("jil99", "jil", "jilson", "humanities student", "edinburgh"),
        ("antonio333", "antonio", "", "NEET", "england"),
        ("tina33", "tina", "murray", "american", "new york"),
        ("beanbagfishman", "tim", "smith", "i like bean bags and i like fishmen", ""),
        ("testUser123", "test", "user", "this is a test account", "")
    ]

    testPosts = [
        ("My first post", "Here are some pictures of my cats", "CatPost.png"),
        ("Looking after fish", "Incredibly relevant question about caring for fish", "fishPost.jpg"),
        ("Looking to sell [Is this the right section?]", "Looking to sell my cat", "catSale.jpg"),
        ("Subscribe to my insta", "I post cat videos on it", "insta.jpeg"),
        ("Find us on facebook", "Search for us", "facebook.png"),
        ("Find us on Twitter", "Search for us", "twitter.png"),
        ("Find us on BeBo", "Search for us", "bebo.jpg"),
        ("First post", "This is a test post", "pufferFish.jpeg")
    ]

    testListings = [
        ("Fluffs", "We are moving so we need to find her a new home", "Cat", "cat.jpg"),
        ("N/A", "Looking to sell lab puppies locally", "Dog", "lab.jpg"),
        ("ExoticFish", "Selling fish", "Fish", "fish.jpeg"),
        ("Daisy", "Cow for sale", "Cow", "cow.jpg"),
        ("Tommy", "Selling my dog", "Dog", "dog.jpg"),
        ("Spy", "Selling a pigeon", "Domestic pigeon", "pigeon.jpg")
    ]

    testPets = [
        ("Dog", "Lab", "There are lots of different types of dogs", "lab.jpg"),
        ("Cow", "Some breed of cow", "There are a few types of cow, this is where we get our milk", "cow.jpg"),
        ("Cat", "Tabby", "Cats are made of yoghurt inside", "cat.jpg"),
        ("Peacock", "Congo peafowl", "Peacocks have like a load of colourful feathers than expand and stuff", "peacock.jpg"),
        ("Pigeon", "Domestic Pigeon", "Pigeons are secretly cameras", "pigeon.jpg")
    ]

    comments = [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut",
        "aliquip ex ea commodo consequat. Duis aute irure dolor ",
        "e cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupida",
        "wow cool",
        "nice!!",
        "very cool",
        "i didnt like this",
        "this is dumb",
        "itecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, ",
        "id ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?",
        "At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores",
        "et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est ",
        "laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi ",
        "optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. ",
        "Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae ",
        "non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut ",
        "perferendis doloribus asperiores repellat.",
        "On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of ",
        "pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame ",
        "ut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia",
        "ostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum",
        "est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.",
        "dipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatu",
        "m. Ut enim ad minima veniam",
        "first"
    ]

    userList = [add_user(user[0], user[1], user[2], user[3], user[4])
                for user in testUsers]
    print("\n")

    petPages = [add_pet(pet[0], pet[1], pet[2], pet[3])
                for pet in testPets]
    print("\n")

    listings = [add_listing(userList, listing[2], listing[0], listing[1], listing[3])
                for listing in testListings]
    print("\n")

    posts = [add_post(userList, post[0], post[1], post[2], comments)
             for post in testPosts]
    print("\n")


def add_user(username, firstName, lastName, bio, location):
    print("New user: " + username)
    newUser = User.objects.get_or_create(
        username = username,
        first_name = firstName,
        last_name = lastName,
        email = "test@test.com"
    )[0]

    newUser.set_password("Test")
    newUser.save()
    newUserProfile = UserProfile.objects.get_or_create(
        user = newUser,
        bio = bio,
        location = location,
    )[0]

    newUserProfile.age = random.randint(5, 80)
    newUserProfile.sellCount = random.randint(0, 50)

    newUserProfile.profilePicture.save("default", ImageFile(open(settings.MEDIA_ROOT + "/population/default.jpg", 'rb')))
    newUserProfile.save()

    return newUserProfile


def add_pet(species, breed, info, image):
    print("New pet-o-pedia: " + breed)
    newPage = PetPedia.objects.get_or_create(
        species = species,
        breed = breed,
        info = info
    )[0]

    newPage.picture.save(image, ImageFile(open(settings.MEDIA_ROOT + "/population/" + image, 'rb')))

    return newPage


def add_post(allUsers, title, description, image, comments):
    print("New post: " + title)
    newPost = Post.objects.get_or_create(
        poster=random.choice(allUsers),
        postTitle = title,
        postDescription = description

    )[0]

    for i in range(0, random.randint(0, 5)):
        newPost.likes.add(random.choice(allUsers).user)

    for i in range(0, random.randint(0, 3)):
        newPost.dislikes.add(random.choice(allUsers).user)

    newPost.postImage.save(image, ImageFile(open(settings.MEDIA_ROOT + "/population/" + image, 'rb')))

    for i in range(0, random.randint(0, 10)):
        randomUser = random.choice(allUsers)

        newComment = Comment.objects.create(
            post = newPost,
            user = randomUser.user,
            content = random.choice(comments)
        )

        newComment.save()

    return newPost


def add_listing(allUsers, breed, name, description, image):
    print("New listing: " + name)
    newListing = Listing.objects.get_or_create(
        breed = breed,
        petName = name,
        description = description,
#        poster=random.choice(allUsers),
#        petAge=random.randint(0, 10),
#        cost=random.randint(0, 150),
        slug = slugify(name),
    )[0]

    newListing.poster = random.choice(allUsers)
    newListing.petAge = random.randint(0, 10)
    newListing.cost = random.randint(0, 150)

    newListing.petImage.save(image, ImageFile(open(settings.MEDIA_ROOT + "/population/" + image, 'rb')))

    return newListing


if __name__ == '__main__':
    print('Starting population script...')
    populate()

