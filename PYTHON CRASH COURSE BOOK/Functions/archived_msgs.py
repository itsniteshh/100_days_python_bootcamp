msgs = ["hello", "hii", "bonjour", "bonsoir", "bonne nuit", "bonne journee"]
sent_msgs = []

def send_messages(msgs):
    
    while msgs:
        sending = msgs.pop()
        print(f"Currently sending {sending}")
        sent_msgs.append(sending)
    
send_messages(msgs[:])


print(msgs)
print(sent_msgs)