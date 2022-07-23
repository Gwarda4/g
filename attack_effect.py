#C:\Users\domi\Desktop\Labirynt_fabularne\dungeons

class AttackEffect:
    
    def __init__(self, attack_target_, attack_aggressor_): #:Entity
        
        self._attack_target_ = attack_target_,
        self._attack_aggressor = attack_aggressor_
    
    def take_hp_from_target(self):
        
        raise NotImplementedError
    
        #zabiera życie self._attack_target_
        
    def take_hp_from_aggressor(self):
            
        raise NotImplementedError
    
        #zabiera życie self._attack_aggressor
    
    def steal_life_from_target(self):
        
        raise NotImplementedError
        
        #zabiera życie self._attack_target_ i oddaje self._attack_aggressor UMIEJĘTNOSC KONKRETNRGO AGRESSORA
        
    def apply_effect_on_target(self):
        
        raise NotImplementedError
    
        #nadaje efekt self._attack_target_
    
    def apply_effect_on_aggressor(self):
        
        raise NotImplementedError
    
        #nadaje efekt self._attack_aggressor UMIEJETNOSC KONKRETNEGO TARGETU
    
    # def return_attack_target(self): # -> Entity
        
    #     raise NotImplementedError
    
    #     #zwraca self._attack_target_
        
    # def return_attack_aggressor(self): # -> Entity
        
    #     raise NotImplementedError
    
    #     #zwraca self._attack_aggressor
        
    # def return_description_of_attack(self) -> self.AttackEffect:
        
    #     raise NotImplementedError
    
    