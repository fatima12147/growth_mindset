
#streamlit

import streamlit as st

st.set_page_config(page_title="Growth Mindset Project⭐")
st.title("Growth Mindset Challenge")

st.header("🚀 Welcome to Your Growth Journey!")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential.This AI-prowered app helps you build a, growth mindset with reflection,challenges,and achievements!⭐")

# quote section:


st.header("💡Today's Growth Mindset Quote")
st.write("Success is not final,failure is not fatal:it is the courage to continus that count.-winston churchill")

st.header("🔧 What's your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")

#conditions:

if user_input:
    st.success(f"🎯You're facing: {user_input}. keep pushing forward your goal!🚀")

else:
    st.warning("Tell us about your challenge to get started!")

#reflection:

st.header("Reflect on Your Learning💪")
st.write("Every experience teaches us something valuable.share a lesson you've learned recently.💡")
reflection = st.text_area("Write your reflection here:") 

if reflection:
    st.success(f"✨Great Insight!Your reflection: {reflection}")

else:
    st.info("Reflecting on pass experience help your grow! your difficulties")

#achievements:

st.header("🏆Celebrate Your Wins!")
achievement =st.text_input("Share something you've recently accomplished:")

if achievement:
    st.success(f"💥Amazing! You achieved: {achievement}")

else:
    st.info("Big or small , every achievement count! share one now⛔")

# footer:

st.write("- - -")
st.write("🗝️growth is a journey of small steps,challenges,and breakthroughs.Stay patient,stay consistent,and focus the process great things take time!⭐") 
st.write("""Create by syeda sehar fatima""")
