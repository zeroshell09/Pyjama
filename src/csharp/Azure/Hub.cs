using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using csharp.Model;
using Microsoft.Azure.Devices;
using Microsoft.Azure.Devices.Client;
using Microsoft.Azure.Devices.Client.Exceptions;
using Newtonsoft.Json;

public class AzureHubConsumer
{
    private readonly string _connstring;
    private readonly string _host;
    private readonly string _endpoint;
    private Dictionary<string, string> _registeredDevices;

    public AzureHubConsumer(string host, string endpoint, string connstring)
    {
        _endpoint = endpoint ?? throw new ArgumentNullException(nameof(endpoint));
        _host = host ?? throw new ArgumentNullException(nameof(host));
        _connstring = connstring ?? throw new ArgumentNullException(nameof(connstring));
        _registeredDevices = new Dictionary<string, string>();
    }

    public async Task Consume(Event e)
    {
        if (!_registeredDevices.ContainsKey(e.DeviceId))
        {
            _registeredDevices[e.DeviceId] = await AddDevice(e.DeviceId);
        }

        var SignalValue = new
        {
            messageId = Guid.NewGuid(),
            deviceId = e.DeviceId,
            x = 1,
            y = e.Data
        };
        
        var messageString = JsonConvert.SerializeObject(SignalValue);
        var azureMEssage = new Microsoft.Azure.Devices.Client.Message(Encoding.UTF8.GetBytes(messageString));
        var deviceClient = DeviceClient.Create(_host, new DeviceAuthenticationWithRegistrySymmetricKey(e.DeviceId, _registeredDevices[e.DeviceId]));

        System.Console.WriteLine($"Pushing : {e.Data}");
        await deviceClient.SendEventAsync(azureMEssage);
    }

    private async Task<string> AddDevice(string deviceId)
    {
        var deviceManager = RegistryManager.CreateFromConnectionString(_connstring);

        Device device;

        try
        {
            device = await deviceManager.AddDeviceAsync(new Device(deviceId));
        }
        catch (DeviceAlreadyExistsException e)
        {
            device = await deviceManager.GetDeviceAsync(deviceId);
            System.Diagnostics.Trace.WriteLine(e);
        }

        return device.Authentication.SymmetricKey.PrimaryKey;
    }
}

