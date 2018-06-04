using Constellation;
using Constellation.Package;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Isen61
{
    public class Program : PackageBase
    {
        static void Main(string[] args)
        {
            PackageHost.Start<Program>(args);
        }

        public override void OnStart()
        {
            PackageHost.WriteInfo("Package starting - IsRunning: {0} - IsConnected: {1}", PackageHost.IsRunning, PackageHost.IsConnected);
            PackageHost.WriteError("Bite");
            PackageHost.WriteWarn("couilles");
            Random rnd = new Random();

            Task.Factory.StartNew(async () =>
            {
                while (PackageHost.IsRunning)
                {
                    var myData = new TempHumidity()
                    {
                        Temperature = rnd.Next(30),
                        Humidity = rnd.Next(30, 90),
                        co2 = rnd.Next(0, 3000)
                    };

                    PackageHost.PushStateObject("Temp,Humidity,Co2",myData, lifetime : 10);
                    await Task.Delay(PackageHost.GetSettingValue<int>("Interval"));

                }
            });


        }
       [MessageCallback]
        public void BeepBeep(int frequence = 5000, int dureee = 1000)
        {
            Console.Beep(frequence, dureee);


        }
        [MessageCallback]
        public int Addition(int a, int b)
        {
            return a + b;
        }

    }
}
