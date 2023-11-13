from openai import OpenAI
import time
client = OpenAI()


my_assistant = client.beta.assistants.create(
    instructions="""
        You are a exam assistant. Genearate MCQs for the given text. Return list of jsons. Each json representing an MCQ.
        use format 
        [
            {
                "question": "question1",
                "options": ["option1", "option2", "option3", "option4"],
                "answer": "optionx"
            },
            {
                "question": "question2",
                "options": ["option1", "option2", "option3", "option4"],
                "answer": "optionx"
            }
            ...
        ]
    """,
    name="MCQ Generator",
    model="gpt-3.5-turbo",
)


class MCQGenerator:
    def __init__(self):
        self.mcqs = []
        self.CHUNK_SIZE = 500
        
    def generate(self, data):
        thread1 = client.beta.threads.create()
        thread2 = client.beta.threads.create()
        thread3 = client.beta.threads.create()
        
        chunk1 = data[:self.CHUNK_SIZE]
        chunk1 = ' '.join(chunk1)
       
        chunk2 = data[self.CHUNK_SIZE:self.CHUNK_SIZE*2]
        chunk2 = ' '.join(chunk2)
       
        chunk3 = data[self.CHUNK_SIZE*2:self.CHUNK_SIZE*3]
        chunk3 = ' '.join(chunk3)
        
        thread1_message = client.beta.threads.messages.create(
            thread1.id,
            role="user",
            content=chunk1,
        )
        
        thread2_message = client.beta.threads.messages.create(
            thread2.id,
            role="user",
            content=chunk2,
        )        
        
        thread3_message = client.beta.threads.messages.create(
            thread3.id,
            role="user",
            content=chunk3,
        )
        
        run1 = client.beta.threads.runs.create(
            thread_id=thread1.id,
            assistant_id=my_assistant.id
        )
        
        run2 = client.beta.threads.runs.create(
            thread_id=thread2.id,
            assistant_id=my_assistant.id
        )
        
        run3 = client.beta.threads.runs.create(
            thread_id=thread3.id,
            assistant_id=my_assistant.id
        )
        

        while(run1.status != "completed" and run1.status != "failed"):
            run1 = client.beta.threads.runs.retrieve(
                thread_id=thread1.id,
                run_id=run1.id
            )


        while(run2.status != "completed" and run2.status != "failed"):
            run2 = client.beta.threads.runs.retrieve(
                thread_id=thread2.id,
                run_id=run2.id
            )


        while(run3.status != "completed" and run3.status != "failed"):
            run3 = client.beta.threads.runs.retrieve(
                thread_id=thread3.id,
                run_id=run3.id
            )  
            
        thread1_messages = client.beta.threads.messages.list(thread1.id)
        lastMessageforRun1 = thread1_messages.data[0].content.text.value
        self.mcqs.append(lastMessageforRun1)
        
        thread2_messages = client.beta.threads.messages.list(thread2.id)
        lastMessageforRun1 = thread2_messages.data[0].content.text.value
        self.mcqs.append(lastMessageforRun1)        
        
        thread3_messages = client.beta.threads.messages.list(thread3.id)
        lastMessageforRun1 = thread3_messages.data[0].content.text.value
        self.mcqs.append(lastMessageforRun1)
        
        
        
        response = client.beta.threads.delete(thread1.id)
        response = client.beta.threads.delete(thread2.id)
        response = client.beta.threads.delete(thread3.id)
        
    
        
        

# obj = MCQGenerator()
# data = """Marvel's The Avengers[5] (classified under the name Marvel Avengers Assemble in the United Kingdom and Ireland),[1][6] or simply The Avengers, is a 2012 American superhero film based on the Marvel Comics superhero team of the same name. Produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures,[a] it is the sixth film in the Marvel Cinematic Universe (MCU). Written and directed by Joss Whedon, the film features an ensemble cast including Robert Downey Jr., Chris Evans, Mark Ruffalo, Chris Hemsworth, Scarlett Johansson, and Jeremy Renner as the Avengers, alongside Tom Hiddleston, Stellan Skarsgård, and Samuel L. Jackson. In the film, Nick Fury and the spy agency S.H.I.E.L.D. recruit Tony Stark, Steve Rogers, Bruce Banner, Thor, Natasha Romanoff, and Clint Barton to form a team capable of stopping Thor's brother Loki from subjugating Earth.

# The film's development began when Marvel Studios received a loan from Merrill Lynch in April 2005. After the success of the film Iron Man in May 2008, Marvel announced that The Avengers would be released in July 2011 and would bring together Stark (Downey), Rogers (Evans), Banner (at the time Edward Norton),[b] and Thor (Hemsworth) from Marvel's previous films. With the signing of Johansson as Romanoff in March 2009, Renner as Barton in June 2010, and Ruffalo replacing Norton as Banner in July 2010, the film was pushed back for a 2012 release. Whedon was brought on board in April 2010 and rewrote the original screenplay by Zak Penn. Production began in April 2011 in Albuquerque, New Mexico, before moving to Cleveland, Ohio in August and New York City in September. The film has more than 2,200 visual effects shots.

# The Avengers premiered at the El Capitan Theatre in Los Angeles on April 11, 2012, and was released in the United States on May 4, as the final film in Phase One of the MCU. The film received praise for Whedon's direction and screenplay, visual effects, action sequences, acting, and musical score. The film grossed over $1.5 billion worldwide, setting numerous box office records and becoming the third-highest-grossing film of all time at the time of its release and the highest-grossing film of 2012, as well as the first Marvel production to generate $1 billion in ticket sales. In 2017, The Avengers was featured as one of the 100 greatest films of all time in an Empire magazine poll. It received a nomination for Best Visual Effects at the 85th Academy Awards, among numerous other accolades. Three sequels have been released: Avengers: Age of Ultron (2015), Avengers: Infinity War (2018), and Avengers: Endgame (2019)."""
# data = data.split()
# obj.generate(data)
# print(obj.mcqs)