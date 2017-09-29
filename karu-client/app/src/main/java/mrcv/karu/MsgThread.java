package mrcv.karu;

import java.io.DataOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.Socket;

public class MsgThread extends Thread{

    //all threads should point to the same server, for now...
    static String host = "192.168.0.100";
    static int port = 10000;

    String message;

    //since run() doesn't take arguments we need to provide the message here
    public MsgThread(String msg) {
        message = msg;
    }

    public void run(){
        enviarMensaje(this.message);
    }

    public void enviarMensaje(String msg)  {
        String processed_msg = processMsg(msg);
        try {
            Socket client = new Socket(host, port);
            OutputStream outToServer = client.getOutputStream();
            DataOutputStream out = new DataOutputStream(outToServer);
            //write UTF sends some weird shit at the beginning
            out.writeBytes(processed_msg);
            client.close();
        }
        catch(IOException e){
            e.printStackTrace();
        }
    }

    //inserts the msg length at the beginning of the string, separated by a comma
    private String processMsg(String msg) {
        return msg.length() + "," + msg;
    }
}