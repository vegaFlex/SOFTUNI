class Player:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = 'Unaffiliated'

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return "Skill already added"

        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        # Correct:
        # result = f"Name: {self.name}" + "\n" + f"Guild: {self.guild}" + "\n"
        # result += f"HP: {self.hp}" + "\n" + f"MP: {self.mp}" + "\n"
        # result += '\n'.join([f"==={skill} - {mana_cost}" for skill, mana_cost in self.skills.items()])
        # return result

        skill_info = '\n'.join([f"==={skill_name} - {mana_cost}" for skill_name, mana_cost in self.skills.items()])
        return f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n{skill_info}"

