import replicate
import json

class Granite():
    def __init__(self, data) -> None:
        self.model = "ibm-granite/granite-3.3-8b-instruct"
        self.data = data
        self.temperature = 0.1
        self.top_p = 0.8
        self.top_k = 40
        self.repetition_penalty = 1.1
    
    def get_prompt(self, data, task) -> str:
        if task == "classify_customer_segment":
            prompt = f"""
            You will be given customer data with RFM number.
            Data: {data.to_string()}

            ### Instruction
            - Before classify the customer, please review the data and understand the context.
            - If the customer is not related to the data, please say "I don't know".
            - Do not include explanations, introductions, or any extra text. Only return the JSON object.
            - One customer one customer, do not classify multiple customers.

            ### Task
            Classify the customer into 4 categories:
            1. Loyal Customers -> Active and buys more than once
            2. Big Spender -> High spenders, even if not recent
            3. New Customers -> Just made their first or recent purchase
            4. At Risk -> Used to buy, but no recent activity
            5. Churned -> Bought long ago, only once

            ### Output
            Respond ONLY in JSON format with the following structure:
            {{
                "Loyal Customers": "List all Loyal Customer Name",
                "Big Spender": "List all Big Spender Customer Name", 
                "New Customers": "List all New Customer Name",
                "At Risk": "List all At Risk Customer Name",
                "Churned": "List all Churned Customer Name",
            }}
            
            """

            return prompt
        
        elif task == "get_customer_profile":
            prompt = f"""
            You will be given data that represent one of the customer segment.

            ### Data
            {data.to_string()}

            ### Instruction
            - Before summarize the data, please review the data and understand the context.
            - If the data is not related to the customer profile, please say "I don't know".
            - Do not include explanations, introductions, or any extra text. Only return the JSON object.

            ### Task
            Summarize the data about customer profile:
            - Majority Region
            - The most used payment method (COD, Credit Card, Debit Card, EFT).
            - The most Product Category.
            - The most Product Name.
            - The most Order Date.
            - The most Quantity.
            - The most Cost per Item.
            - The most Sale Price.

            ### Output
            Respond in JSON format with the following structure:
            {{
                "Majority Region": "Region Name",
                "Payment Method": {{"Most": "Payment Method", "Least": "Payment Method"}},
                "Product Category": {{"Most": "Product Category", "Least": "Product Category"}},
                "Product Name": {{"Most": "Product Name", "Least": "Product Name"}},
                "Order Date": {{"Most": "Order Date", "Least": "Order Date"}},
                "Quantity": {{"Most": "Quantity", "Least": "Quantity"}},
                "Cost per Item": {{"Most": "Cost per Item", "Least": "Cost per Item"}},
                "Sale Price": {{"Most": "Sale Price", "Least": "Sale Price"}}
            }}
            """
            return prompt
        
        elif task == "summarize_customer_profile":
            prompt = f"""
            You will be given data that provide all customer profile.

            ### Data
            {data}

            ### Instruction
            - Before summarize the data, please review the data and understand the context.
            - If the data is not related to the customer profile, please say "I don't know".
            - Do not include explanations, introductions, or any extra text. Only return in json format.

            ### Task
            Summarize the data about customer profile.

            ### Output
            Respond in JSON format with the following structure:
            {{
                "Loyal Customers": "summary of loyal customers",
                "Big Spender": "summary of big spender",
                "New Customers": "summary of new customers",
                "At Risk": "summary of at risk customers",
                "Churned": "summary of churned customers",
            }}
            """
            return prompt
        
        elif task == "get_customer_persona":
            prompt = f"""
            You will be given customer profile summary.

            ### Data
            {data}

            ### Instruction
            - Do not include explanations, introductions, or any extra text. Only return in json format.
            - For each customer segment please identify the persona type, key traits, average purchase, and buyer characteristic.

            ### Task
            Identify customer persona of each customer segment with following requirements:
            - Persona type -> example, One-Time High-Intent Purchaser, Trial Buyer, etc
            - Key traits -> example,  Consistent category purchases (Hats), Bulk buying (avg 7 items), Uses credit card, Moderate-high spending, etc
            - Average purchase -> example, $1,000
            - Buyer characteristic -> example, Brand-attached, Quality-focused, Less price-sensitive, etc

            ### Output
            Respond ONLY in JSON format with the following structure:
            {{
                "Loyal Customers": {{"persona_type": "Persona type", "key_traits": "Key traits", "average_purchase": "Average purchase", "buyer_characteristic": "Buyer characteristic"}},
                "Big Spender": {{"persona_type": "Persona type", "key_traits": "Key traits", "average_purchase": "Average purchase", "buyer_characteristic": "Buyer characteristic"}},
                "New Customers": {{"persona_type": "Persona type", "key_traits": "Key traits", "average_purchase": "Average purchase", "buyer_characteristic": "Buyer characteristic"}},
                "At Risk": {{"persona_type": "Persona type", "key_traits": "Key traits", "average_purchase": "Average purchase", "buyer_characteristic": "Buyer characteristic"}},
                "Churned": {{"persona_type": "Persona type", "key_traits": "Key traits", "average_purchase": "Average purchase", "buyer_characteristic": "Buyer characteristic"}},
            }}
            """
            return prompt

        elif task == "get_recommendation":
            prompt = f"""
            You will be given buyer persona data.

            ### Data
            {data}

            ### Instruction
            - Do not include explanations, introductions, or any extra text. Only return in json format.
            - For each buyer persona please identify the recommendation action.
            - You can give multiple recommendation actions.

            ### Task
            Identify recommendation action of each buyer persona.

            ### Output
            Respond ONLY in JSON format with the following structure:
            {{
                "Loyal Customers": "Recommendation action",
                "Big Spender": "Recommendation action",
                "New Customers": "Recommendation action",
                "At Risk": "Recommendation action",
                "Churned": "Recommendation action",
            }}
            """
            return prompt


    def parse_output(self, output) -> dict:
        reformat = ''.join(output) if isinstance(output, (list, tuple)) else str(output)
        return json.loads(reformat)
    
    def classify_customer_segment(self, data):
        prompt = self.get_prompt(data,task="classify_customer_segment")
        response = replicate.run(
            self.model, 
            input={'prompt': prompt, 
                    'temperature': self.temperature,
                    'top_p': self.top_p,
                    'top_k': self.top_k,
                    'repetition_penalty': self.repetition_penalty
                }
        )
        parsed = self.parse_output(response)
        return parsed

    def get_customer_profile(self, data):
        prompt = self.get_prompt(data,task="get_customer_profile")
        response = replicate.run(
            self.model, 
            input={'prompt': prompt, 
                    'temperature': self.temperature + 0.1,
                    'top_p': self.top_p,
                    'top_k': self.top_k,
                    'repetition_penalty': self.repetition_penalty
                }
        )
        parsed = self.parse_output(response)
        return parsed
    
    def summarize_customer_profile(self, data):
        prompt = self.get_prompt(data,task="summarize_customer_profile")
        response = replicate.run(
            self.model, 
            input={'prompt': prompt, 
                    'temperature': self.temperature + 0.1,
                    'top_p': self.top_p,
                    'top_k': self.top_k,
                    'repetition_penalty': self.repetition_penalty
                }
        )
        parsed = self.parse_output(response)
        return parsed
    
    def get_customer_persona(self, data):
        prompt = self.get_prompt(data,task="get_customer_persona")
        response = replicate.run(
            self.model, 
            input={'prompt': prompt, 
                    'temperature': self.temperature + 0.1,
                    'top_p': self.top_p,
                    'top_k': self.top_k,
                    'repetition_penalty': self.repetition_penalty
                }
        )
        parsed = self.parse_output(response)
        return parsed
    
    def get_recommendation(self,data):
        prompt = self.get_prompt(data,task="get_recommendation")
        response = replicate.run(
            self.model, 
            input={'prompt': prompt, 
                    'temperature': self.temperature + 0.1,
                    'top_p': self.top_p,
                    'top_k': self.top_k,
                    'repetition_penalty': self.repetition_penalty
                }
        )
        parsed = self.parse_output(response)
        return parsed