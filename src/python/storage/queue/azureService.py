from azure.storage.queue import QueueService


class AzureQueue:
    
    def __init__(self,accountName,key):
        
        """
            Initialize a new connection to azure queue stoage

            @param accountName : the storage account in azure
            @param key : the api key
        """
        
        self._accountName = accountName
        self._key = key
        self._innerService = QueueService(account_name=self._accountName, account_key=self._key)
    
    def push_message(self,queue,message):

        """
            Enqueue a new message into the given queue

            @param queue : the queue name
            &param message : the message to put into the queue

        """

        if not queue:
            raise ValueError("queue name is mandatory ")

        if not message:
            raise ValueError("message is mandatory")
            
        self._innerService.put_message(queue,message)


    