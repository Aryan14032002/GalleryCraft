from PIL import Image, ImageDraw, ImageFont
import requests
import streamlit as st
import os

#write about art ex-- manadala, pencil sketch,face sketch, 

import base64
painting_ratings = {
    "Radha Krishna Mandala Art": 0,
    "Mahadev Pencil Sketch": 0,
    "Maa Durga Sketch": 0,
    "Sri Ganesh Mandala Art": 0,
    "Krishna Radha Sketch": 0,
    "Freedom Fighters Sketch": 0,
    "Virat Kohli Sketch": 0,
    "Commissioned Sketch": 0
}

watermark_text = "Aryan art Work"
def add_text_watermark(image_path, output, x_position = 300 , y_position = 600):
    draw = ImageDraw.Draw(image_path)
    font = ImageFont.load_default()
    font_size = 40
    font = ImageFont.truetype("DelaGothicOne-Regular.ttf", font_size)
    position = (x_position, y_position)          
    text_color = (128, 128, 128)
    image_path.save(output)
    draw.text(position,watermark_text, font=font, fill=text_color)
    
st.set_page_config(page_title="GalleryCraft", page_icon="icon.png", layout="wide")

file_ = open("Stary_nights.gif", "rb")       #Vincent van Gogh make this stary nights picture 
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()
def load_lottieurl(url):
    r= requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
img_gif =Image.open("Stary_nights.gif") 
img_achievment= Image.open("My achievement.jpg")
img_krishnaradha=Image.open("image (1).jpg")
img_krishnaradha=img_krishnaradha.resize((1000,600))
img_mahadev=Image.open("IMG_20210508_162336_727.jpg")
img_mahadev=img_mahadev.resize((1000,1200))
img_maa_durga=Image.open("IMG_20210703_223828_598.jpg")
img_maa_durga = img_maa_durga.resize((1000, 1000))
img_shree_ganesh=Image.open("20201225_222015.jpg")
img_shree_ganesh=img_shree_ganesh.resize((1000,1200))
img_krishnaradha_sketch=Image.open("Adobe Scan 18 Oct 2021_1.jpg")
img_krishnaradha_sketch=img_krishnaradha_sketch.resize((1000,1200))
img_freedom_fighter_sketch=Image.open("Aryan kumar CSE-f (10)_1 (2).jpg")
img_freedom_fighter_sketch=img_freedom_fighter_sketch.resize((1000,1200))
img_viratkohli_sketch=Image.open("20201113_214329.jpg")
img_viratkohli_sketch=img_viratkohli_sketch.resize((1000,1200))
img_commissioned_sketch=Image.open("IMG_20220910_102928_818.jpg")
img_commissioned_sketch  = img_commissioned_sketch.resize((1000,1200))
img_myphoto=Image.open("my photo.jpg")
img_myphoto = img_myphoto.resize((120, 120))  

add_text_watermark(img_commissioned_sketch,"commissioned_sketch.jpg")
add_text_watermark(img_freedom_fighter_sketch,"commissioned_freedom_sketch.jpg")
add_text_watermark(img_krishnaradha_sketch,"commissioned_krishnaradha_sketch.jpg")
add_text_watermark(img_maa_durga,"commissioned_maadurga_sketch.jpg", y_position=500)
add_text_watermark(img_mahadev,"commissioned_mahadev_sketch.jpg")
add_text_watermark(img_shree_ganesh,"commissioned_shreeGanesh_sketch.jpg")
add_text_watermark(img_viratkohli_sketch,"commissioned_ViratKohli_sketch.jpg")
add_text_watermark(img_krishnaradha,"commissioned_kr_sketch.jpg", y_position= 300)

paintings_by_category = {
    "Sketch": [img_krishnaradha_sketch, img_freedom_fighter_sketch, img_maa_durga,img_mahadev],
    "Mandala": [img_shree_ganesh,img_krishnaradha],
    "Face sketches": [img_commissioned_sketch, img_viratkohli_sketch],
    "Printed Drawings": [img_krishnaradha_sketch,img_krishnaradha, img_freedom_fighter_sketch, img_viratkohli_sketch,img_mahadev,img_shree_ganesh, img_maa_durga],
}




with st.container():
     left_column, right_column = st.columns(2)
     with left_column:
       st.title("Hi folks, Dive into a world of boundless creativity. :wave:",)
       st.header("Artistry by Aryan Kumar: Sketches & Mandalas")
       st.markdown("""Welcome to my world of sketches and Mandalas.<br>I'm  ARYAN KUMAR, an artist weaving tales of <br>  tranquility through intricate designs. Explore the <br> magic where every line holds a story, and each <br>  Mandala is a portal to inner serenity. Join me in <br>this journey of mindfulness and artistry.""", unsafe_allow_html=True)

st.write("[see my Linkedin profile >](https://www.linkedin.com/in/aryan-kumar-26480820a)")



with right_column:
        st.markdown( f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',unsafe_allow_html=True)
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I have gained in this field")
        st.write('##')
        st.markdown("""
            <h3 style="text-align: justify;">Picture Perfect Achievement</h3>
            <p style="text-align: justify;">In a gathering of talented artists from various colleges,
               I proudly clinched the top spot in sketching.
               It's a moment that fills me with immense joy and pride.
               This achievement is a testament to my passion and dedication to the art form.
               I look forward to continuing this journey of creativity and self-expression.
            </p>
        """, unsafe_allow_html=True)
    with right_column:
        st.image(img_achievment)
with st.container():
    st.write("---")
    st.header("Select category of paintings")
    st.write('##')
# Create a dropdown menu
selected_category = st.selectbox("Please choose the category of painting you are interested in, and kindly provide the name of the painting you want to purchase in the contact form below", ["Select Category"] + list(paintings_by_category.keys()), key="category_dropdown")

# Display the images based on the selected category
if selected_category != "Select Category":
    paintings = paintings_by_category.get(selected_category, [])
    if paintings:
        st.header(selected_category)
        st.markdown('<div style="display: flex; overflow-x: auto;">', unsafe_allow_html=True)
        for i, painting in enumerate(paintings):
            st.image(painting, width=200, caption=f"{selected_category} Painting")

            # Add rating form
            st.subheader(f"Rate {selected_category} Painting {i+1} (1-10)")
            rating = st.slider("", 0, 10, 0, key=f"rating_{selected_category}_{i}")
            painting_ratings[f"{selected_category} Painting {i+1}"] = rating

        st.markdown('</div>', unsafe_allow_html=True)

# Add JavaScript to hide/show paintings based on category selection
st.write("""
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const select = document.querySelector('select[name="category_dropdown"]');
            select.setAttribute('readonly', 'readonly');
            select.addEventListener('click', function() {
                this.size=1;
            });
            select.addEventListener('blur', function() {
                this.size=0;
            });
            select.addEventListener('change', function() {
                const selectedCategory = this.value;
                const paintings = document.querySelectorAll('.painting-container');
                paintings.forEach(painting => {
                    if (painting.dataset.category === selectedCategory) {
                        painting.style.display = 'inline-block';
                    } else {
                        painting.style.display = 'none';
                    }
                });
            });
        });
    </script>
""", unsafe_allow_html=True)
with st.container():
    st.write("---")
    st.header("Artistry for Sale: Explore My Creations")
    st.write('##')
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_krishnaradha)
    with text_column:
        st.subheader("RADHA KRISHNA MANDALA ART")
        st.write(" This captivating mandala intricately weaves the eternal love story of Krishna and Radha.",unsafe_allow_html=True)
        with st.expander("Read more about this mandala"):
            st.write("Flanking the central figures are two resplendent and graceful peacocks, their vibrant plumage echoing the celestial romance that unfolds at the heart of this mesmerizing artwork.<br>It is of 120 cm wide and 50 cm long<br>The price of the art work ranges from 2000 rs to 4000 rs.",unsafe_allow_html=True)  
with st.container():
    image_column, text_column = st.columns((1,2))   
    with image_column:
        st.image(img_mahadev)
    with text_column:
        st.subheader("MAHADEV PENCIL SKETCH")
        st.write("In this striking and intricate pencil sketch, Lord Shiva's presence is vividly captured.",unsafe_allow_html=True) 
        with st.expander("Read more about this sketch"):
            st.write("The artist's meticulous detailing brings out the intensity in his gaze and the serenity in his demeanor. The play of light and shadow adds depth, breathing life into this divine portrayal. The trident and crescent moon, symbols of his cosmic authority, stand tall in this depiction.This sketch is not just art; it's a moment of quiet reverence in the presence of a cosmic deity. It invites viewers to reflect on the profound significance of Mahadev in Hindu cosmology, offering a tangible connection to the divine.<br>The size is 50 cm long and 30 cm wide<br>The price of this artwork ranges from 500 rs to 1000rs",unsafe_allow_html=True )

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_maa_durga)
    with text_column:
        st.subheader("MAA DURGA SKETCH")
        st.write( "This captivating, intricate sketch beautifully portrays the divine countenance of Maa Durga.",unsafe_allow_html=True)
        with st.expander("Read more about this sketch"):
            st.write("The artist skillfully captures her grace and strength, with meticulous attention to detail. Symbolic elements like the third eye and crescent moon add depth to the depiction, creating a sense of reverence and connection to her boundless power.<br>The size of this art is 40 cm wide and 30 cm long.<br>The price of this art ranges from 500 rs to 700 rs",unsafe_allow_html=True)
with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_shree_ganesh)
    with text_column:
        st.subheader("SRI GANESH MADALA ART")
        st.write("This stunning and intricate mandala art piece beautifully captures the essence of Lord Ganesh.",unsafe_allow_html=True)
        with st.expander("Read more about this mandala"):
             st.write("The intricate details delicately form the visage of the benevolent deity, emphasizing his iconic elephantine features and serene countenance. The gentle curvature of the mandala frames Lord Ganesh's face with a sense of harmony, mirroring the balance and wisdom he embodies.<br>Each stroke of this mandala reflects the artist's profound reverence for Lord Ganesh, portraying him with the utmost respect and devotion. The use of vibrant colors and precise lines further enhances the spiritual aura surrounding this portrayal. This mandala art not only showcases the artist's skill but also serves as a powerful visual meditation, inviting viewers to connect with the divine energy that Lord Ganesh represents.<br>The size of the art is 30 cm wide and 50 cm long.<br>The price of this art is 300 rs to 500 rs.",unsafe_allow_html=True)
        
with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_krishnaradha_sketch)
    with text_column:
        st.subheader("KRISHNA RADHA SKETCH ")
        st.write("This exquisite and detailed sketch beautifully portrays the eternal love between Krishna Radha.",unsafe_allow_html=True) 
        with st.expander("Read more about this mandala"):
             st.write("The artist's skilled hand brings forth the divine essence of these two beloved figures. Krishna, with his iconic flute and enchanting presence, stands beside Radha, their eyes locked in a gaze that transcends mortal understanding.The intricate details in their attire and expressions convey a deep sense of emotion and devotion. The play of light and shadow adds depth, giving the sketch a three-dimensional quality that brings the divine couple to life. This sketch not only captures the essence of their timeless love story but also invites viewers to contemplate the profound spiritual connection between individual souls and the divine, creating a moment of quiet reflection in their presence..<br>This sketch is 40 cm wide and 60cm long.<br>The price of this sketch ranges from 700 rs to 1000 rs",unsafe_allow_html=True)
with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_freedom_fighter_sketch)
    with text_column:
        st.subheader("FREEDOM FIGHTERS SKECTH")
        st.write("This poignant pencil sketch pays tribute to the valiant souls who fought for India's independence.",unsafe_allow_html=True)
        with st.expander("Read more about this sketch"):
            st.write("It is framed by the iconic tricolor flag. Each figure stands tall, embodying the spirit of sacrifice and determination that defined this historic era.<br>The artist's meticulous detailing brings out the strength and resolve etched in the faces of these freedom fighters. Their eyes reflect a burning passion for a free nation, while the folds of the Indian flag flutter with a sense of victory and hope. The interplay of light and shadow imparts depth, creating a powerful visual narrative that speaks to the courage and unity of those who paved the way for India's liberation.This sketch is not merely a work of art; it is a tribute to the indomitable spirit that led India to its hard-fought freedom. It invites viewers to reflect on the sacrifices made and the triumphs achieved, leaving an indelible mark on the nation's history.<br>This sketch is of a4 size.<br>This sketch ranges from 250 rs to 500 rs.",unsafe_allow_html=True)
with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_viratkohli_sketch)
    with text_column:
        st.subheader("VIRAT KOHLI SKETCH")
        st.write("In this striking sketch, the left-profile of the iconic cricketer Virat Kohli is beautifully rendered.",unsafe_allow_html=True) 
        with st.expander("Read more about this sketch"):
            st.write("The artist's meticulous attention to detail captures every contour, from the sharp lines of his jaw to the intense gaze that defines his competitive spirit. The play of light and shadow adds depth, giving the sketch a lifelike quality that seems to breathe with the energy and determination for which Kohli is renowned.The sketch not only celebrates Virat Kohli's athletic prowess but also invites viewers to connect with the human side of this cricketing legend. It offers a moment of quiet reflection on the dedication and passion that have made him a symbol of sporting excellence, inspiring countless fans around the world.<br>This sketch is of A4 size.<br>The face sketch ranges from 250 rs to 500 rs.",unsafe_allow_html=True)
with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_commissioned_sketch)
    with text_column:
        st.subheader("COMMISSIONED SKETCH")
        st.write("This artwork is a personalized masterpiece, meticulously crafted to bring the client's vision to life.",unsafe_allow_html=True) 
        with st.expander("Read more about this sketch"):
            st.write("It embodies the collaborative process between artist and client, resulting in a bespoke creation that holds personal significance and lasting value.<br>This art is in A3 size.<br>The price of commissioned art work depend on its size and number of faces, for this size the price ranges from 300 rs to 500 rs",unsafe_allow_html=True)
        
        
with st.container():
    st.write("---")
    st.header("FAQ")
    st.write('##')

    with st.expander("Question 1: What is the price range for your artworks?"):
        st.write("The price range for my artworks varies depending on the size and complexity of the piece. "
                 "You can find specific pricing details in the description of each artwork above.")
    with st.expander("Question 2: How can I purchase an artwork?"):
        st.write("To purchase an artwork, please use the contact form below and specify the name of the artwork you're interested in. ""I will get in touch with you to discuss further details.")
    with st.expander("Question 3: Can I customize my Art based on my vision?"):
        st.write("Of course! Feel free to share your preferences and any specific details about the type of art you envision in the message box below. Your input is invaluable in crafting a piece that truly resonates with your vision and preferences.")
    with st.expander("Question 4: What is the turnaround time for custom commissions?"):
        st.write("See,the turnaround time of each artwork is intricately linked to its unique attributes. Factors such as the size, complexity, and whether it's a portrait sketch or a mandala all play a significant role. For instance, in the case of face sketches, the number of faces and the level of detail required are crucial considerations. This level of attention to detail ensures that the final piece is a true reflection of the vision and preferences of each client.")
    with st.expander("Question 5: Do you offer framing or packaging options for your artwork?"):
        st.write("Yes, I provide framing and packaging options for my artwork to enhance the overall presentation and ensure it arrives in excellent condition. Clients can choose from a selection of high-quality frames that complement the style of the artwork.")
with st.container():
    st.write("---")
    st.header("To purchase the art or for any enquiry contact me on the given details")
    st.write('##')
    contact_form="""
    <div style = "height:300px ; width:100%;">
      <form action="https://formsubmit.co/aryan10kumar11@gmail.com" method="POST" style = "display:block;">
      <div style = " display : flex; justify-content:space-evenly; height: 40px ">
       <input type="text" name="name" placeholder="Your name" size = 40 required >
       <input type="email" name="email" placeholder="Your email" size = 40 required >
      </div> 
      <div style = "display:flex; justify-content:space-evenly; height : 40px;">
       <input type name="message" placeholder="Interested in purchasing or customizing art? Write your message or preferences here."  size = 104 required > 
      </div> 
      <div style = "display:flex;  justify-content:center; ">
       <button type="submit" style = "height: 40px ;width: 70px;">Send</button>
       </div>
    </form>
    </div>"""
    st.markdown(contact_form, unsafe_allow_html=True)
    
with st.container():
    st.write("---")
    st.image(img_myphoto)
    st.subheader("My contact number is -- 9304264007.")
    st.write("Follow me on")
    st.write("[ My Instagram >](https://instagram.com/itz._.me._.aryan._?igshid=MzMyNGUyNmU2YQ==)")
    st.write("[ My Facebook >](https://www.facebook.com/profile.php?id=100044592585213&mibextid=ZbWKwL)")
    st.write("[ My Twitter >](https://x.com/aryan10kumar11?s=09)")
    
with st.container():
    st.write("---")   
    st.header("Feedback Form")
    name, email = st.columns(2)
    with name:
        name_input = st.text_input("Name")
    
    with email:
        email_input = st.text_input("Email (Optional)")
    feedback = st.text_input("Feedback")
    submitted = st.button("Submit Feedback")
    if submitted and feedback and name_input:
        st.success("Thank you for your feedback!")
        with open("feedback.txt", "a") as file:
            file.write(f"Name: {name_input}\n")
            if email_input:
                file.write(f"Email: {email_input}\n")
            file.write(f"Feedback: {feedback}\n")
    elif submitted:
        st.warning("Please provide both feedback and name before submitting.")
        
with st.container():
    st.write("---")
    # st.header("Welcome to My Art Gallery")
    st.header("[ About me >](https://aryan14032002.github.io/about_me/)")

    
  


