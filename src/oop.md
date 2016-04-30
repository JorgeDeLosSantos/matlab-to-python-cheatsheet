## Object-Oriented Programming
<!-- ==================== TOC using MarkdownTOC Sublime-Text plugin ===================== -->
<!-- MarkdownTOC depth=3 -->

- Defining class

<!-- /MarkdownTOC -->
<!-- ==============================  END TOC ================================= -->

<!-- ============================= PRE ================================= -->

### Defining class

General syntax:

```matlab
classdef MyClass
% Help of class
% 
    properties
        % class properties
    end

    methods
        function obj = MyClass(args)
            % Constructor
        end

        % other methods
        function OneMethod(obj,one_args)
            % Method ...
        end

        function OtherMethod(obj,other_args)
            % Method ...
        end
    end
end
```

```python
class MyClass():
    def __init__(self,args):
        # Constructor
        # Class properties are defined here

    def OneMethod(self,one_args):
        # Method

    def OtherMethod(self,other_args):
        # Method
```

