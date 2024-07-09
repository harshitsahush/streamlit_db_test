import streamlit as st
from sqlalchemy.sql import text

conn = st.connection("pets_db", type = "sql")

with conn.session as s:
    s.execute(text("CREATE TABLE IF NOT EXISTS pet_owners (person TEXT, pet TEXT)"))
    s.execute(text("DELETE FROM pet_owners"))
    pet_owners = {"jerry" : "fish", "harry" : "cow", "garry" : "fox"}
    for key in pet_owners:
        s.execute(
            text("INSERT INTO pet_owners (person, pet) VALUES (:owner, :pet)"),
            params = dict(owner = key, pet = pet_owners[key])
        )
    s.commit()

response = conn.query("SELECT * FROM pet_owners")
st.dataframe(response)