package mrcv.karu;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void buttonClicked(View v){
        //todo: some kind of check if connection is not possible at startup!
        MsgThread worker;
        switch (v.getId()){
            case R.id.btnPlayPause:
                worker=new MsgThread("playpause");
                break;
            case R.id.btnPrevious:
                worker=new MsgThread("prevtrack");
                break;
            case R.id.btnNext:
                worker=new MsgThread("nexttrack");
                break;
            case R.id.btnVolumeDown:
                worker=new MsgThread("volumedown");
                break;
            case R.id.btnVolumeUp:
                worker=new MsgThread("volumeup");
                break;
            default:
                Toast.makeText(getApplicationContext(),"Botón no existente!", Toast.LENGTH_SHORT).show();
                //we return to avoid calling run() on a null object
                return;
        }
        worker.start();
    }
}
