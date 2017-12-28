using System;
using System.IO;
using System.Threading;
using System.Threading.Tasks;
using csharp.Model;
using Microsoft.Extensions.Configuration;

namespace csharp
{
    class Program
    {
        public static IConfigurationRoot configuration { get; set; }
        static void Main(string[] args)
        {

            configuration = new ConfigurationBuilder()
            .SetBasePath(Directory.GetCurrentDirectory())
            .AddJsonFile("appsettings.json").Build();

            var host = configuration["host"];
            var connstring = configuration["connstring"];
            var endpoint = configuration["endpoint"];

            var sensor = new VirtualSensor(Guid.NewGuid().ToString());
            var hub = new AzureHubConsumer(host, endpoint, connstring);
            var cancellationToken = new CancellationToken();
            sensor.AddConsumer(e => hub.Consume(e).Wait());
            Task.Factory.StartNew(sensor.Start, cancellationToken).Wait();
        }
    }
}
