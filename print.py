from David import say
def Hello_World_Java():
    java = """public class HelloWorld{
    public static void main(String[]args){
        System.out.println("Hello world!!");
    }
}"""
    file = open('HelloWorld.java','w')
    file.write(java+ "\n")
    say("hello world in java printed successfully.")
    
def Hello_World_Python():
    python = """print("Hello World!")"""
    file = open('HelloWorld.py','w')
    file.write(python + "\n")
    say("hello world in python printed successfully.")
                
            