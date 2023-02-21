from typing import Union, Dict, List, Optional, Tuple

import flwr as fl
from flwr.server.client_manager import ClientManager
from flwr.server.client_proxy import ClientProxy

from torch.utils.tensorboard import SummaryWriter


class TensorboardStrategy(fl.server.strategy.FedAvg):
    def __repr__(self) -> str:
        return "TensorboardStrategy"

    def __init__(
        self,
        min_fit_clients,
        min_available_clients,
        fraction_fit,
        eval_fn,
        writer,
        on_fit_config_fn):

        super().__init__(min_fit_clients=min_fit_clients, 
                        min_available_clients=min_available_clients, 
                        fraction_fit=fraction_fit,
                        evaluate_fn=eval_fn,
                        on_fit_config_fn=on_fit_config_fn)
        
        self.writer = writer

    def evaluate(self, server_round, parameters):
        """Evaluate model parameters using an evaluation function."""
        loss, metrics = super().evaluate(server_round, parameters)

        # Write scalars
        self.writer.add_scalar("Training/test_loss", loss, server_round)
        self.writer.add_scalar("Training/test_accuracy", metrics["accuracy"], server_round)
        self.writer.add_scalar("Training/test_c_loss", metrics["c_loss"], server_round)

        return loss, metrics
