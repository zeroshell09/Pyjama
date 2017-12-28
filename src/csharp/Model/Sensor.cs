using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;

namespace csharp.Model
{
    public class VirtualSensor
    {
        public string Id { get; private set; }
        private readonly int _frequency;
        private Action<Event> _consumer;

        public VirtualSensor(string id, int frequency = 100)
        {
            this.Id = id;
            this._frequency = frequency;
        }

        public void AddConsumer(Action<Event> consumer)
        {
            _consumer = consumer;
        }

        public void Start()
        {
            var counter = 0.0;

            while (true)
            {

                var ev = new Event
                {
                    DeviceId = this.Id,
                    Data = Process(counter).ToString()
                };

                _consumer(ev);

                Thread.Sleep(_frequency);

                counter+=0.01;
            }
        }

        private static double Process(double value)
        {
            return value * Math.Sin(value);
        }
    }
}