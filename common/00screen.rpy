# Screen system support.

init python:
    
    class Return(Action):
        def __init__(self, value=True, hide=True):
            self.value = value
            self.hide = hide

        def __call__(self):
            if hide:
                renpy.hide_screen(renpy.current_screen())

            return self.value

    class Jump(Action):

        def __init__(self, label, hide=True):
            self.label = label
            self.hide = hide

        def __call__(self):
            
            if hide:
                renpy.hide_screen(renpy.current_screen())

            renpy.jump(label)
                    
    class Show(Action):
        def __init__(self, screen):
            self.screen = screen

        def __call__(self):
            renpy.show_screen(self.screen)
            renpy.restart_interaction()
            
        def get_selected(self):
            return renpy.showing(self.screen)

    class Hide(Action):
        def __init__(self, screen):
            self.screen = screen

        def __call__(self):
            renpy.hide_screen(self.screen)
            renpy.restart_interaction()
            
            
        
    ##########################################################################
    # Functions that set variables or fields.

    # class Set(Action):
    #     def __init__(self, var, value):
    #         self.var = var
    #         self.value = value

    #     def __call__(self)
    #         renpy.get_current_screen().scope[self.var] = self.value
    #         renpy.restart_interaction()

    #     def get_selected(self):
    #         return renpy.get_current_screen().scope[self.var] == self.value
        
    class SetField(Action):
        def __init__(self, obj, var, value):
            self.object = obj
            self.var = var
            self.value = value
        
        def __call__(self):
            setattr(self.object, self.var, self.value)
            renpy.restart_interaction()

        def get_selected(self):
            return getattr(self.object, self.var) == self.value
                
    def SetVariable(var, value):
        return SetField(store, var, value)

    def SetPreference(var, value):
        return SetField(_preferences, var, value)
    
    # class Toggle(Action):
    #     def __init__(self, var):
    #         self.var = var

    #     def __call__(self)
    #         renpy.get_current_screen().scope[self.var] = not renpy.get_current_screen().scope[self.var]
    #         renpy.restart_interaction()

    #     def get_selected(self):
    #         return renpy.get_current_screen().scope[self.var]
        
    class ToggleField(Action):
        def __init__(self, obj, var):
            self.object = obj
            self.var = var
        
        def __call__(self):
            setattr(self.object, self.var, not getattr(self.object, self.var))
            renpy.restart_interaction()

        def get_selected(self):
            return getattr(self.object, self.var)
               
    def ToggleVariable(var):
        return SetField(store, var)

    def TogglePreference(var):
        return SetField(_preferences, var)

    
    
    