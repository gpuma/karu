package mrcv.karu;

import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Toast;

import java.io.DataOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.Socket;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void btnProbarClicked(View v){
        if(v.getId()==R.id.btn_probar){
            Toast.makeText(getApplicationContext(),"Me tocaste!", Toast.LENGTH_SHORT).show();
            (new MsgThread()).start();
        }
    }

    class MsgThread extends Thread{

        String host = "192.168.0.100";
        int port = 10000;

        public void run(){
            enviarMensaje("Te la comes toda!");
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
}
