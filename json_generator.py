import json
import random


# Generate 10 random first names
sample_first_names = [
    "John", "Alice", "Max", "Meghan", "Sam", "Stacy", "Peter", "Mary", "George", "Sally"
]

# Generate 10 random last names
sample_last_names = [
    "Smith", "Jones", "Williams", "Brown", "Wilson", "Taylor", "Johnson", "White", "Martin", "Anderson"
]

# Generate 3 random universities
sample_universities = [
    "University of California, Berkeley",
    "University of California, Los Angeles",
    "University of California, San Diego"
]

# Generate 3 random schools
sample_schools = [
    "School of Engineering",
    "School of Arts and Sciences",
    "School of Business"
]

simu_data = []
sime_data = []


def main():
    for i in range(20):
        first_name = random.choice(sample_first_names)
        last_name = random.choice(sample_last_names)
        simu_data.append({
            "id": random.randint(100000000, 999999999),
            "first_name": first_name,
            "last_name": last_name,
            "university": random.choice(sample_universities),
            "email": first_name.lower() + last_name.lower() + "@uni.edu",
            "birthday": str(random.randint(1, 28)) + str(random.randint(1, 12)) + str(random.randint(1990, 2000))
        })

    for i in range(20):
        first_name = random.choice(sample_first_names)
        last_name = random.choice(sample_last_names)
        sime_data.append({
            "id": random.randint(100000000, 999999999),
            "first_name": first_name,
            "last_name": last_name,
            "school": random.choice(sample_schools),
            "email": first_name.lower() + last_name.lower() + "@school.edu",
            "birthday": str(random.randint(1, 28)) + str(random.randint(1, 12)) + str(random.randint(2000, 2010))
        })

    simu_file = open("samples/simu.json", "w")
    sime_file = open("samples/sime.json", "w")
    simu_file.write(json.dumps(simu_data, indent=4))
    sime_file.write(json.dumps(sime_data, indent=4))
    simu_file.close()
    sime_file.close()

    simu_id_file = open("samples/simu_id.txt", "w")
    sime_id_file = open("samples/sime_id.txt", "w")
    for i in range(20):
        simu_id_file.write(str(simu_data[i]["id"]) + "\n")
        sime_id_file.write(str(sime_data[i]["id"]) + "\n")
    simu_id_file.close()
    sime_id_file.close()

    print(json.dumps(simu_data, indent=4))
    print(json.dumps(sime_data, indent=4))


if __name__ == '__main__':
    main()
