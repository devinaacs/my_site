# Create your views here.

from datetime import date
from django.shortcuts import render

all_posts = [
    {
        "slug": "dataran-merdeka-kuala-lumpur",
        "image": "dataran_merdeka.jpg",
        "author": "Dev",
        "date": date(2024, 3, 31),
        "title": "Dataran Merdeka, Kuala Lumpur",
        "excerpt": "Discover the historical significance and vibrant atmosphere of Dataran Merdeka in Kuala Lumpur.",
        "content": """
            Dataran Merdeka, or Independence Square, is a historical landmark in Kuala Lumpur that played a pivotal role in Malaysia's journey to independence. The square is surrounded by colonial-era buildings, including the Sultan Abdul Samad Building, which adds to its historical charm. Visitors can explore the rich history of Malaysia by visiting the nearby museums and galleries. The square is also a popular venue for national events and celebrations, providing a lively and patriotic atmosphere. Whether you are a history enthusiast or simply looking to soak in the local culture, Dataran Merdeka is a must-visit destination in Kuala Lumpur.
        """
    },
    {
        "slug": "adventures-in-genting-highlands",
        "image": "genting_highlands.jpg",
        "author": "Dev",
        "date": date(2024, 4, 1),
        "title": "Adventures in Genting Highlands",
        "excerpt": "Explore the thrills, natural beauty, and entertainment options in Genting Highlands.",
        "content": """
            Genting Highlands, located just an hour away from Kuala Lumpur, is a popular hill resort known for its cool climate, theme parks, and entertainment options. One of the main attractions is the Genting SkyWorlds Theme Park, offering a variety of thrilling rides and attractions for visitors of all ages. The resort is also home to a world-class casino, luxurious hotels, and a wide range of dining options. The Awana SkyWay, a scenic cable car ride, provides stunning views of the surrounding mountains and lush rainforest. For nature enthusiasts, the Chin Swee Caves Temple, nestled in a serene environment, offers a peaceful retreat with its beautiful architecture and panoramic views. Genting Highlands also hosts numerous live performances and shows, making it a vibrant destination for entertainment. Whether you are seeking adventure, relaxation, or entertainment, Genting Highlands has something to offer for everyone.
        """
    },
    {
        "slug": "exploring-johor-bahru",
        "image": "johor_bahru.jpg",
        "author": "Dev",
        "date": date(2024, 4, 2),
        "title": "Exploring Johor Bahru",
        "excerpt": "Uncover the cultural and historical attractions of Johor Bahru.",
        "content": """
            Johor Bahru, the capital city of Johor, is a vibrant city rich in cultural and historical attractions. Visitors can explore the Sultan Abu Bakar State Mosque, an architectural masterpiece, or visit the Royal Abu Bakar Museum to learn about the royal family's history. The city is also known for its bustling markets, such as the Johor Bahru Night Market, where you can find a variety of local foods and handmade goods. For families, the nearby LEGOLAND Malaysia Resort offers a fun-filled day of activities. Johor Bahru's blend of modern amenities and historical charm makes it an ideal destination for all types of travelers.
        """
    },
    {
        "slug": "discovering-geylang",
        "image": "geylang.jpg",
        "author": "Dev",
        "date": date(2024, 4, 3),
        "title": "Discovering Geylang",
        "excerpt": "Experience the unique culture and culinary delights of Geylang, Singapore.",
        "content": """
            Geylang, located just outside Singapore's city center, is a neighborhood known for its vibrant culture and diverse culinary scene. The area is famous for its food, particularly the local hawker stalls that offer a wide range of delicious dishes such as beef kway teow and durian. Geylang is also home to several historic buildings and temples, providing a glimpse into Singapore's rich heritage. The lively atmosphere and unique character of Geylang make it a must-visit destination for those looking to experience a different side of Singapore.
        """
    },
    {
        "slug": "china-town-singapore",
        "image": "china_town.jpg",
        "author": "Dev",
        "date": date(2024, 4, 4),
        "title": "China Town, Singapore",
        "excerpt": "Explore the rich history and vibrant streets of Chinatown in Singapore.",
        "content": """
            Chinatown in Singapore is a bustling district filled with rich history and vibrant culture. The area is known for its traditional shophouses, temples, and street markets. Visitors can explore the Buddha Tooth Relic Temple, which houses a sacred relic of the Buddha, or wander through the Chinatown Heritage Centre to learn about the lives of early Chinese immigrants. The streets of Chinatown are also lined with stalls selling everything from souvenirs to local delicacies. With its lively atmosphere and deep cultural roots, Chinatown is a fascinating destination for anyone visiting Singapore.
        """
    },
    {
        "slug": "merlion-park-singapore",
        "image": "merlion_park.jpg",
        "author": "Dev",
        "date": date(2024, 4, 5),
        "title": "Merlion Park, Singapore",
        "excerpt": "Visit the iconic Merlion Park and enjoy stunning views of Singapore's skyline.",
        "content": """
            Merlion Park is one of Singapore's most famous landmarks, featuring the iconic Merlion statue, which is a symbol of the city. Located near Marina Bay, the park offers breathtaking views of the city's skyline and is a popular spot for tourists and locals alike. Visitors can take photos with the Merlion statue, enjoy a leisurely stroll along the waterfront, or simply relax and take in the scenic views. The park's central location makes it an ideal starting point for exploring other attractions in the area, such as Marina Bay Sands and the Esplanade. Merlion Park is a must-visit for anyone looking to experience the essence of Singapore.
        """
    },
    {
        "slug": "changi-airport-singapore",
        "image": "changi_airport.jpg",
        "author": "Dev",
        "date": date(2024, 4, 6),
        "title": "Changi Airport, Singapore",
        "excerpt": "Experience world-class amenities and entertainment at Changi Airport, Singapore.",
        "content": """
            Changi Airport is not just an airport, but a world-class destination in itself. Consistently ranked as one of the best airports in the world, Changi offers an array of amenities and entertainment options for travelers. From the stunning Jewel Changi complex with its indoor waterfall and lush gardens to the various themed lounges and relaxation areas, there is something for everyone. The airport also features a wide range of dining and shopping options, making it a perfect place to unwind before or after a flight. Changi's efficient services and top-notch facilities ensure a seamless and enjoyable travel experience for all visitors.
        """
    }
]


def get_date(post):
    return post['date']


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, 'blog/all-posts.html')


def post_detail(request, slug):
    return render(request, 'blog/post-detail.html')
