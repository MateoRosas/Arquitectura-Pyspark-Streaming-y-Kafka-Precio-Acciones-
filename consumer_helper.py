from kafka import KafkaConsumer
import json

if __name__ == "__main__":
   consumer = KafkaConsumer(
      "registered_user",
      bootstrap_servers='ip-172-31-12-245.ec2.internal:9092',
           auto_offset_reset='earliest',
      group_id="consumer-group-a")

print("starting the consumer")
for msg in consumer:
   print("Registered user = {}".format(json.loads(msg.value)))
